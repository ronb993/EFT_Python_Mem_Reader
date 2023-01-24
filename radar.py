from eft_data import EFT
import time

def main():
    
    eft = EFT()
    eft.find_gameworld()
    eft.get_lgw_ptr()
    eft.get_registered_players()
    while True:
        time.sleep(1)
        eft.update_registered_players()



if __name__ == '__main__':
    main()