# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 05/03/2024 15:45
# Last change preformed by     : Danny
# Last change (Description)    : Created the header for the .py files.
# ---------------------------------------------------------------------------------------

# Here we import the required functions and classes
import player
import functions
import os
import time
import colorama
import dialogue

players = []

functions.introscreen()
os.system("cls")
functions.menuscreen()

valid_player = False

while not valid_player:
    player_count = input(f"<{colorama.Fore.BLUE}SYSTEM{colorama.Style.RESET_ALL}>  With how many player would you like to play? : ")
    if player_count.isnumeric() and 0 < int(player_count) <= 4:
        player_count = int(player_count)
        for i in range(player_count):
            temp_playername = input(f"<{colorama.Fore.BLUE}SYSTEM{colorama.Style.RESET_ALL}>  Player {(i + 1)} what is your name? : ")
            new_player = player.Player()
            new_player.set_username(temp_playername)
            new_player.set_playername(f"p{(i + 1)}")
            players.append(new_player)
        valid_player = True
    else:
        print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}>  INVALID PLAYER COUNT GIVEN, PLEASE USE A VALID PLAYER COUNT BETWEEN 2 AND 4")
        time.sleep(3)
        os.system("cls")
        functions.menuscreen()

game_running = True

while game_running:
    for i in players:
        can_create_rocket = functions.rocketcheck(i)
        can_fuel_rocket = functions.rocketfuelcheck(i)
        if can_create_rocket and can_fuel_rocket:
            launch_rocket = False
            valid_rocketlaunch_reponse = False
            while not valid_rocketlaunch_reponse:
                input_rocket_launch = input(f"<{colorama.Fore.GREEN}SYSTEM{colorama.Style.RESET_ALL}> {colorama.Fore.GREEN}ROCKET IS READY FOR LAUNCH, DO YOU WISH TO LAUNCH YOUR ROCKET?{colorama.Style.RESET_ALL} (Y/N) : ")
                if input_rocket_launch.isalpha() and input_rocket_launch.upper() in ["Y", "N"]:
                    if input_rocket_launch.upper() == "Y":
                        launch_rocket = True
                        valid_rocketlaunch_reponse = True
                    else:
                        launch_rocket = False
                        valid_rocketlaunch_reponse = True
                else:
                    print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}> {colorama.Fore.RED}INVALID INPUT, PLEASE GIVE A VALID INPUT{colorama.Style.RESET_ALL}")
        elif can_create_rocket and not can_create_rocket:
            curr_fuellevel = i.get_curr_fuellevel()
            if curr_fuellevel >= 90:
                print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}> {colorama.Fore.RED}REQUIRED FUEL LEVEL NEARLY ACQUIRED. NEEDED FUEL UNTIL ABLE TO LAUNCH{colorama.Style.RESET_ALL} : \"{colorama.Fore.RED + (curr_fuellevel - 100) + colorama.Style.RESET_ALL}\"")
        else:
            functions.board(i)

            i.update_turns_used()

os.system("cls")
functions.credits()
