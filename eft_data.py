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
    
    def update(self):
        pass

    def update_misc(self):
        pass

    def ptr_chain(self, base, offsets) -> int:
        try:
            addr = base
            for offset in offsets[:-1]:
                addr = pm.read_ulonglong(addr + offset)
            return addr + offsets[-1]
        except Exception as e:
            print(e)

    def get_gameworld_ptr(self, gom):
        print("Running loop until raid starts....")
        object_name = ""
        while object_name != "GameWorld":
            active_node = pm.read_ulonglong(gom + Offsets.active_node)
            if active_node != 0:
                try:
                    obj_ptr = pm.read_ulonglong(active_node + Offsets.active_node_ptr)
                    object_name_ptr = pm.read_ulonglong(obj_ptr + Offsets.unity_object_name)
                    object_name = pm.read_string(object_name_ptr)
                    if object_name == "GameWorld":
                        print(f'You Found GameWorld: {object_name}')
                        return obj_ptr

                except Exception as e:
                     print(e)
                     continue
            else:
                 return "cannot find active node"

    def get_lgw(self):
            try:
                gameworld_ptr = self.get_gameworld_ptr(self.gom)
                lgw = self.ptr_chain(gameworld_ptr, offsets=Offsets.lgw_ptrchain)
                print(f'LGW Address Found: {hex(lgw)}')
                return lgw

            except Exception as e:
                print("Cannot find game world, restart game")
                sys.exit(e)
    

    def get_registered_players(self):
        lgw = self.get_lgw()
        self.lgw_ptr = pm.read_ulonglong(lgw)
        registered_player_ptr = pm.read_ulonglong(self.lgw_ptr + Offsets.reg_players)
        player_size = pm.read_int(registered_player_ptr + Offsets.reg_player_count)
        return player_size
    
    def update_registed_players(self):
        registered_player_ptr = pm.read_ulonglong(self.lgw_ptr + Offsets.reg_players)
        player_size = pm.read_int(registered_player_ptr + Offsets.reg_player_count)
        return player_size

