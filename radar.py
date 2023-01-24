from eft_data import EFT
import time

def main():
    
    eft = EFT()
    if not(eft.object_loop_ran):
        if(eft.find_gameworld()):
            print('Game World Found!')
        if(eft.get_lgw_ptr()):
            print("Local Game World found!")
        if(eft.get_registered_players() < 1):
            print("Searching for Registered Players")
            
    while True:
        time.sleep(12)
        if (eft.update_registered_players()):
            players = eft.update_registered_players()
            if int(players) > 1:
                print(f'Registered Players: {players}')



if __name__ == '__main__':
    main()