import pymem
import pymem.process
from pymem.process import module_from_name
from pymem.ptypes import RemotePointer
import time

gom_pointer = 0x17FFD28
pm = pymem.Pymem("EscapeFromTarkov.exe")
game_module = module_from_name(pm.process_handle, "UnityPlayer.dll").lpBaseOfDll

def get_gom():
    gom_addr = game_module + gom_pointer
    gom = pm.read_ulonglong(gom_addr)
    print(f'Found Game Module at {hex(game_module)}')
    print(f'GOM Addr found at {hex(gom)}')
    return gom

def ptr_chain(base, offsets) -> int:
    try:
        addr = base
        for offset in offsets[:-1]:
            addr = pm.read_ulonglong(addr + offset)
        return addr + offsets[-1]
    except Exception as e:
        print(e)


def get_object_from_list(gom):
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

def get_lgw():
        lgw_ptrchain = [0x30, 0x18, 0x28]
        try:
            gameworld_ptr = get_object_from_list(get_gom())
            time.sleep(5)
            lgw = ptr_chain(gameworld_ptr, offsets=lgw_ptrchain)
            #lgw_ptr = pm.read_ulonglong(lgw)
            return lgw

        except Exception as e:
            print(e)           

def get_registered_players():
    lgw_ptr = get_lgw()
    time.sleep(5)
    registered_players = pm.read_ulonglong(lgw_ptr + 0x90)
    reg_size_ptr = registered_players + 0x18
    reg_size = pm.read_uint(reg_size_ptr)
    return reg_size


players_registered = get_registered_players()
print(players_registered)


