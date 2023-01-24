from eft_data import EFT
import time

def main():
    
    eft = EFT()
    player_count = eft.get_registered_players()
    print(player_count)
    while True:
        time.sleep(5)
        print(eft.update_registed_players())


if __name__ == '__main__':
    main()