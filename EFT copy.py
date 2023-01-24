import pymem, pymem.process, sys, time
from pymem.process import module_from_name
from helper import Offsets

try:
    pm = pymem.Pymem("EscapeFromTarkov.exe")
    game_module = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll
except Exception as e:
    sys.exit(e)


# Run after loading EFT
class EFT:
    def __init__(self):
        self.gom_addr = game_module + Offsets.gom_offset
        self.gom = pm.read_ulonglong(self.gom_addr)
        if self.gom:
            print(f'GOM Address found: {hex(self.gom)}')
    

    def ptr_chain(self, base, offsets) -> int:
        try:
            addr = base
            for offset in offsets[:-1]:
                addr = pm.read_ulonglong(addr + offset)
            return addr + offsets[-1]
        except Exception as e:
            print(e)


    def get_object_from_list(self, gom):
        while True:
            time.sleep(1)
            active_node = pm.read_ulonglong(gom + 0x20)
            if active_node != 0:
                for i in range(0, 1000):
                    try:
                        obj_ptr = pm.read_ulonglong(active_node + 0x10)
                        object_name_ptr = pm.read_ulonglong(obj_ptr + 0x60)
                        object_name = pm.read_string(object_name_ptr)
                        if object_name == "GameWorld":
                            print(f'You found: {object_name}')
                            print(f'Game World Pointer: {hex(obj_ptr)}')
                            return obj_ptr
                        else:
                            active_node = pm.read_ulonglong(active_node)

                    except Exception as e:
                        print(f'active_node = {active_node}, unreadable breaking out')
                        break

    def get_lgw(self):
            lgw_ptrchain = [0x30, 0x18, 0x28]
            try:
                gameworld_ptr = get_object_from_list(get_gom())
                time.sleep(5)
                lgw = ptr_chain(gameworld_ptr, offsets=lgw_ptrchain)
                #lgw_ptr = pm.read_ulonglong(lgw)
                return lgw

            except Exception as e:
                print(e)           

    def get_registered_players(self):
        lgw_ptr = get_lgw()
        time.sleep(5)
        registered_players = pm.read_ulonglong(lgw_ptr + 0x90)
        reg_size_ptr = registered_players + 0x18
        reg_size = pm.read_uint(reg_size_ptr)
        return reg_size


players_registered = get_registered_players()
print(players_registered)


