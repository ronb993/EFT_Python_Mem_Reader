from eft_data import EFT
import time

def main():
    
    eft = EFT()
    if eft.object_loop_ran == False:
        if(eft.find_gameworld()):
            print(Game World Found!)
    eft.get_lgw_ptr()
    eft.get_registered_players()
    while True:
        time.sleep(12)
        players = eft.update_registered_players()
        if int(players) > 1:
            print(f'Registered Players: {players}')



if __name__ == '__main__':
    main()