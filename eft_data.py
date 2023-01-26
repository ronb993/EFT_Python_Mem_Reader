import pymem, pymem.process, sys, time
from pymem.process import module_from_name
from helper import Offsets

try:
    pm = pymem.Pymem("EscapeFromTarkov.exe")
    game_module = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
except Exception as e:
    sys.exit(e)

class EFT:
    def __init__(self):
        self.gom_addr = game_module + Offsets.gom_offset
        self.gom = pm.read_ulonglong(self.gom_addr)
        if self.gom:
            print(f'GOM Address found: {hex(self.gom)}')
        self.lgw_ptr = 0
        self.registered_player_ptr = 0
        self.obj_ptr = 0
        self.object_loop_ran = False
        self.gameworld_ptr = 0
        self.reg_players = 0
        self.player_size = 0

    def ptr_chain(self, base, offsets) -> int:
        try:
            addr = base
            for offset in offsets[:-1]:
                addr = pm.read_ulonglong(addr + offset)
            return addr + offsets[-1]
        except Exception as e:
            print(e)

    def run_objects_loop(self, gom, name):
        print("Running loop until raid starts....")
        object_name = ""
        while object_name != name:
            active_node = pm.read_ulonglong(gom + Offsets.active_node)
            if active_node != 0:
                try:
                    self.obj_ptr = pm.read_ulonglong(active_node + Offsets.active_node_ptr)
                    object_name_ptr = pm.read_ulonglong(self.obj_ptr + Offsets.unity_object_name)
                    object_name = pm.read_string(object_name_ptr)
                    if object_name == name:
                        self.object_loop_ran = True
                        return self.obj_ptr

                except Exception as e:
                     continue
            else:
                 return "cannot find active node"

    def find_gameworld(self):
        if not self.object_loop_ran:
            self.gameworld_ptr = self.run_objects_loop(self.gom, "GameWorld")
            return self.gameworld_ptr
        else:
            print("Secon iteration of runnning object loop")

    def get_lgw_ptr(self):
            try:
                self.lgw_ptr = self.ptr_chain(self.gameworld_ptr, offsets=Offsets.lgw_ptrchain)
                return self.lgw_ptr

            except Exception as e:
                print("Cannot find game world, restart game")
                sys.exit(e)

    def get_registered_players(self):
        lgw = pm.read_ulonglong(self.lgw_ptr)
        print(hex(lgw))
        self.registered_player_ptr = pm.read_ulonglong(lgw + Offsets.reg_players)
        self.player_size = pm.read_int(self.registered_player_ptr + Offsets.reg_player_count)
        return self.player_size

    def update_registered_players(self):
        self.player_size = pm.read_int(self.registered_player_ptr + Offsets.reg_player_count)
        return self.player_size
    
