# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 05/03/2024 15:45
# Last change preformed by     : Danny
# Last change (Description)    : Created the header for the .py files.
# ---------------------------------------------------------------------------------------

# Here we import the required functions, classes and dialogue
import os
import time
import colorama
import dialogue
import trivia
import random


def introscreen():
    intro = dialogue.intro_dialogue
    select_space_center = random.randint(0, 11)

    random_number = ""
    if select_space_center != 12:
        while len(random_number) != 5:
            random_int = random.randint(0, 9)
            random_number += str(random_int)
    else:
        random_number = "69420"

    space_port = f"{colorama.Fore.GREEN}SPACE CENTER:{colorama.Fore.BLUE} {dialogue.spaces_centers[select_space_center]}{colorama.Fore.GREEN} - COMMUNICATION SYSTEMS - COMMUNICATION POD: {colorama.Fore.CYAN}#{random_number}{colorama.Style.RESET_ALL}"

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"

    print(space_port)
    print(underscore)
    print(f"<{colorama.Fore.BLUE}SYSTEM{colorama.Style.RESET_ALL}>  USER:<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> CONNECTED TO COMMUNICATION SYSTEMS - ACCESS LEVEL: {colorama.Fore.RED}UNKNOWN{colorama.Style.RESET_ALL}")
    for i in intro:
        time.sleep(3)
        print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> {i}")

    time.sleep(5)
    print(f"<{colorama.Fore.BLUE}SYSTEM{colorama.Style.RESET_ALL}>  USER:<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> DISCONNECTED FROM COMMUNICATION SYSTEMS")
    time.sleep(5)
    input("Press ENTER to continue...")
    print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}>  {colorama.Fore.RED}ERROR{colorama.Style.RESET_ALL}: {colorama.Fore.RED}REMOTE SYSTEM BREACHED COMMUNICATIONS SYSTEM{colorama.Style.RESET_ALL}")
    time.sleep(2)
    print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}>  {colorama.Fore.RED}REMOTE COMMAND RECEIVED{colorama.Style.RESET_ALL}, COMMAND GIVEN: {colorama.Fore.RED}SUDO DELETE_MESSAGES{colorama.Style.RESET_ALL}, AUTHORITY: {colorama.Fore.MAGENTA}SYSTEM_ADMIN{colorama.Style.RESET_ALL}")
    print(f"<{colorama.Fore.RED}SYSTEM{colorama.Style.RESET_ALL}>  {colorama.Fore.RED}DELETING ALL MESSAGES{colorama.Style.RESET_ALL}")
    time.sleep(5)

def menuscreen():
    game_logo = dialogue.game_logo

    # print(colorama.Back.BLUE + colorama.Fore.WHITE + f"{game_logo[0]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.RED + colorama.Fore.WHITE + f"{game_logo[1]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.MAGENTA + colorama.Fore.WHITE + f"{game_logo[2]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.CYAN + colorama.Fore.WHITE + f"{game_logo[3]}" + colorama.Style.RESET_ALL)
    # print(colorama.Back.BLUE + colorama.Fore.WHITE + f"{game_logo[4]}" + colorama.Style.RESET_ALL)

    print(colorama.Fore.BLUE + f"{game_logo[0]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + f"{game_logo[1]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.MAGENTA + f"{game_logo[2]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"{game_logo[3]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + f"{game_logo[4]}" + colorama.Style.RESET_ALL)
    print(colorama.Fore.RED + f"{game_logo[5]}" + colorama.Style.RESET_ALL)
    print(f"Version: 1.0 (07/03/2024)")
    print(f"Project by: <{colorama.Fore.MAGENTA}Sogaand Momayez{colorama.Style.RESET_ALL}>, <{colorama.Fore.YELLOW}Julian Gonzalez Verbeek{colorama.Style.RESET_ALL}>, <{colorama.Fore.RED}Danny de Snoo{colorama.Style.RESET_ALL}>\n\n\n")


def credits():
    credit = dialogue.intro_dialogue
    select_space_center = random.randint(0, 12)

    random_number = ""
    while len(random_number) != 5:
        random_int = random.randint(0, 9)
        random_number += str(random_int)

    space_port = colorama.Fore.GREEN + "SPACE STATION: " + colorama.Fore.BLUE + dialogue.spaces_centers[
        select_space_center] + colorama.Fore.GREEN + " - COMMUNICATION SYSTEMS - COMMUNICATION POD: " + colorama.Fore.CYAN + "#" + random_number + colorama.Style.RESET_ALL

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"


def rocketcheck(curr_player):
    players_rocketparts = curr_player.get_curr_rocketparts_list()

    heatshield = 0
    avionics = 0
    control_systems = 0
    fuel_tank = 0
    engines = 0
    fuselage = 0
    communication_system = 0
    unknown = 0

    for i in players_rocketparts:
        if i == "HEATSHIELD":
            heatshield += 1
        elif i == "AVIONICS":
            avionics += 1
        elif i == "CONTROL_SYSTEMS":
            control_systems += 1
        elif i == "FUEL_TANK":
            fuel_tank += 1
        elif i == "ENGINES":
            engines += 1
        elif i == "FUSELAGE":
            fuselage += 1
        elif i == "COMMUNICATION_SYSTEM":
            communication_system += 1
        else:
            unknown += 1

    if heatshield > 0 and avionics > 0 and control_systems > 0 and fuel_tank > 0 and engines > 0 and fuselage > 0 and communication_system > 0:
        return True
    else:
        return False


def rocketfuelcheck(curr_player):
    players_fuellevel = curr_player.get_curr_rocketparts_list()

    if players_fuellevel == 100:
        return True
    else:
        return False


def shop(curr_player):
    selected_shop_logo = random.randint(0, 5)
    shoplogo = dialogue.shop_logos[selected_shop_logo]
    os.system("cls")

    line = ""
    for i in shoplogo[0]:
        line += "="

    print(colorama.Fore.BLUE + line + colorama.Style.RESET_ALL)
    for i in shoplogo:
        print(colorama.Fore.CYAN + i + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + line + colorama.Style.RESET_ALL)

    selected_shop_keeper = random.randint(0, 5)
    shopkeeper = dialogue.shop_keepers[selected_shop_keeper]

    shopkeeper_fullname = shopkeeper[0]
    shopkeeper_name = shopkeeper[1]
    shopkeeper_dialogue = shopkeeper[2]

    print(f"{colorama.Fore.GREEN}SHOP KEEPER{colorama.Style.RESET_ALL} : <{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}>")
    print(colorama.Fore.BLUE + line + colorama.Style.RESET_ALL + "\n")

    for i in shopkeeper_dialogue:
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_name}{colorama.Style.RESET_ALL}> {i}")

    print("\n")
    print("Options: BUY (Buy a part for 2500 imperial credits), SELL (Sell a part for 1500 imperial credits), CONTINUE\n")

    Choice = ""
    valid_choice = False
    while not valid_choice:
        input_choice = input(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> ")

        if input_choice.isalpha() and input_choice.upper() == "BUY":
            Choice = "BUY"
            valid_choice = True
        elif input_choice.isalpha() and input_choice.upper() == "SELL":
            Choice = "SELL"
            valid_choice = True
        elif input_choice.isalpha() and input_choice.upper() == "CONTINUE":
            Choice = "CONTINUE"
            valid_choice = True
        else:
            print(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> Whoops, i didn't use valid option. I am going to retry that")

    if Choice == "BUY":
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> What would you like to buy?")
        parts_list = ""
        for i in dialogue.rocket_parts:
            if parts_list == "":
                parts_list = i
            else:
                parts_list += f", {i}"

        options = dialogue.rocket_parts
        options.append("EXIT")

        exit = False
        while not exit:
            purchase_options = ""
            for e in options:
                if purchase_options == "":
                    purchase_options = e
                else:
                    purchase_options += f", {e}"

            print(purchase_options)

            input_buy = input(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> ")

            valid_option = False
            for o in options:
                if input_buy.upper() == o:
                    valid_option = True
                if input_buy.upper() == "EXIT":
                    exit = True
                    valid_option = True

            if valid_option and not exit:
                buy_rocketpart(curr_player, curr_player.get_curr_money(), input_buy.upper(), shopkeeper_fullname)
            else:
                print(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> Whoops, i didn't use valid option. I am going to retry that")

    elif Choice == "SELL":
        print(f"<{colorama.Fore.CYAN}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> What would you like to sell?")

        exit = False
        while not exit:
            options = curr_player.get_curr_rocketparts_list()
            options.append("EXIT")

            options_str = ""
            for i in options:
                if options_str == "":
                    options_str = i
                else:
                    options_str += f", {i}"

            print(f"options: {options_str}")
            input_sell = input(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> ")

            valid_option = False
            for o in options:
                if input_sell.upper() == o:
                    valid_option = True
                if input_sell.upper() == "EXIT":
                    exit = True
                    valid_option = True

            if valid_option and not exit:
                sell_rocketpart(curr_player, input_sell, shopkeeper_fullname)
            else:
                print(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> Whoops, i didn't use valid option. I am going to retry that")

    else:
        print(
            f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> See you later! <{colorama.Fore.CYAN}{shopkeeper_fullname}{colorama.Style.RESET_ALL}>")


def fuelstation(curr_player):
    selected_fuelstation_logo = random.randint(0, 4)
    fuelstationlogo = dialogue.fuelstation_logos[selected_fuelstation_logo]
    os.system("cls")

    line = ""
    for i in fuelstationlogo[0]:
        line += "="

    print(colorama.Fore.BLUE + line + colorama.Style.RESET_ALL)
    for i in fuelstationlogo:
        print(colorama.Fore.CYAN + i + colorama.Style.RESET_ALL)
    print(colorama.Fore.BLUE + line + colorama.Style.RESET_ALL)

    print("\n")
    print("Options: BUY (Buy 10% fuel for 2000 imperial credits), CONTINUE\n")

    Choice = ""
    valid_choice = False
    while not valid_choice:
        input_choice = input(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> ")

        if input_choice.isalpha() and input_choice.upper() == "BUY":
            Choice = "BUY"
            valid_choice = True
        elif input_choice.isalpha() and input_choice.upper() == "CONTINUE":
            Choice = "CONTINUE"
            valid_choice = True
        else:
            print(f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> Whoops, i didn't use valid option. I am going to retry that")

    if Choice == "BUY":
        current_money = curr_player.get_curr_money()

        if current_money >= 2000:
            curr_player.remove_money(2000)
            curr_player.add_fuellevel(10)

            print(f"<{colorama.Fore.GREEN}FUEL STATION{colorama.Style.RESET_ALL}> {colorama.Fore.GREEN}PURCHASE SUCCESFULL{colorama.Style.RESET_ALL}, CURRENT FUEL LEVEL: {curr_player.get_curr_fuellevel()}")
            valid_choice = True
        else:
            print(f"<{colorama.Fore.RED}FUEL STATION{colorama.Style.RESET_ALL}> {colorama.Fore.RED}PURCHASE UNSUCCESFULL{colorama.Style.RESET_ALL}, PLEASE {colorama.Fore.RED}LEAVE{colorama.Style.RESET_ALL} THE FUELING STATION")
            valid_choice = True
    else:
        print(
            f"<{colorama.Fore.YELLOW}{curr_player.get_username()}{colorama.Style.RESET_ALL}> Okay, lets continue")

def fallen_star(curr_player):
    rocket_parts = ["HEATSHIELD", "AVIONICS", "CONTROL SYSTEMS", "FUEL TANK", "ENGINES", "FUSELAGE",
                    "COMMUNICATION SYSTEM"]
    random_item = rocket_parts[random.randrange(7)]

    fallen_star = random.randrange(1, 3)
    if fallen_star == 1:
        curr_player.add_rocketparts(random_item)
        print(f">Oh...? You spot something sparkling behind a rock\n\
>It appears to be a fallen star!\n\
>You find '{random_item}'")
    elif fallen_star == 2:
        curr_player.add_rocketparts(random_item)
        print(f">You trip over something shiny\n\
>A fallen star! Neat!\n\
>You find '{random_item}'")
    else:
        curr_player.add_rocketparts(random_item)
        print(f">As you make a stop you see something crashing before your feet\n\
>A fallen star!\n\
>You find '{random_item}'")


def training_field(curr_player):
    # decides which game is going to be played
    which_game = random.randrange(0, 2)

    if which_game == 1:  # TRIVIA
        print(">Trivia Time!\n\
>Let's get those brains working")
        question = random.randrange(30)  # generates a random question
        print(trivia.trivia[question][0])  # print the question

        #  checks if the user input is Valid
        while True:
            user = input(">Enter Your Answer... ")
            user_upper = user.upper()
            if user_upper == "A" or user_upper == "B" or user_upper == "C":
                break
            else:
                print("Input Error! Please Answer With 'A', 'B' or 'C'!")

        # rewards or penalizes the player
        if user_upper == trivia.trivia[question][1]:
            print(">CORRECT! HERE IS YOUR REWARD: 2000 Imperial Credits")  # give reward
            curr_player.add_money(2000)
        else:
            print(f">INCORRECT!, The Correct Answer Is {trivia.trivia[question][1]}!")  # penalty the player
            if curr_player.get_curr_money() < 1000:  # check if the player is able to lose 2500
                curr_player.remove_money(curr_player.get_curr_money())  # removes all of the players money
                print(">All of your Imperial Credits have been removed")
            else:
                curr_player.remove_money(1000)  # removes set amount of money from the player
                print(">You have lost 1000 Imperial credits!")

    else:  # HANGMAN
        print(">Hangman time!\n\
>Guess the letters to find the right word")
        usable_word = False

        while not usable_word:
            difficulty = input(">Select difficulty (1-5): ")
            if difficulty.isnumeric():
                if 1 <= int(difficulty) <= 5:
                    word = trivia.hangman[int(difficulty) - 1][random.randrange(5)]
                    usable_word = True
                else:
                    print(">Please select a valid difficulty!")
            else:
                print(">Please select a valid difficulty!")

        # assign correct reward onto the difficulty chosen
        if difficulty == 1:
            prize = 500
            penalty = 250
        elif difficulty == 2:
            prize = 1000
            penalty = 500
        elif difficulty == 3:
            prize = 1500
            penalty = 750
        elif difficulty == 4:
            prize = 2000
            penalty = 1000
        else:
            prize = 2500
            penalty = 1250

        is_playing = True
        guessed_letters_count = 0
        mistakes = 0
        letter_array = []
        guessed_letters_array = []

        for letter in word:
            letter_array += "_"

        while is_playing:
            is_correct_guess = False
            is_guessed_letter = False

            print(letter_array)

            letter_input = input(">Choose a Letter: ").upper()

            for letter in guessed_letters_array:  # Check if letter is guessed
                if letter_input == letter:
                    is_guessed_letter = True
                    print(">You Already Guessed: " + letter)
                    break

            if is_guessed_letter == False:  # Only add the letter if its not already guessed
                guessed_letters_array += letter_input  # Add the letter in the guessed letters

            for letter_index in range(len(word)):  # Check if its the right letter
                if letter_input == word[letter_index] and not is_guessed_letter:
                    letter_array[letter_index] = letter_input
                    is_correct_guess = True
                    guessed_letters_count += 1

            if is_correct_guess == False:
                mistakes += 1
                print(">UNLUCKY. Mistakes: " + str(mistakes) + " Try Again")

            if guessed_letters_count == len(word):
                print(f">YOU WIN! The Word Was: {word}\n\
>You win: {prize} Imperial Credits")
                curr_player.add_money(prize)
                is_playing = False

            if mistakes == 8:
                if penalty > curr_player.get_curr_money():
                    curr_player.remove_money(curr_player.get_curr_money())
                    print(f">GAME OVER! The word was: {word}\n\
>You lose all of your Imperial Credits")
                    is_playing = False
                else:
                    print(f">GAME OVER! The word was: {word}\n\
>You lose: {penalty} Imperial Credits")
                    curr_player.remove_money(penalty)
                    is_playing = False


def random_event(curr_player):
    rocket_parts = ["HEATSHIELD", "AVIONICS", "CONTROL SYSTEMS", "FUEL TANK", "ENGINES", "FUSELAGE",
                    "COMMUNICATION SYSTEM"]

    # makes sure the player has an equal chance to either win or lose something
    fifty_fifty = random.randrange(2)

    if fifty_fifty == 0:
        random_item = rocket_parts[random.randrange(7)]
        print(f">You stumble upon a wreckage of an ancient alien spaceship\n\
>Amid the twisted metals you find a rocket part! '{random_item}'! That is perfect for your spacecraft!\n\
>It seems fortune smiles upon you")
        curr_player.add_rocketparts(random_item)  # adds a random item to the players inventory
    else:
        typeLoss = random.randrange(3)
        if typeLoss == 1:  # loses rocketpart
            item_count = len(curr_player.get_curr_rocketparts_list())  # check inventory
            if item_count == 0:  # to check if he has something to lose
                print(">You get hit in the head by an asteroid!\n\
    >Luckily you don't own anything and you lose nothing")
            else:
                item_position = random.randrange(item_count + 1)  # choses random item
                item_lost = curr_player.get_curr_rocketparts_pos(item_position)  # sets up the removal
                curr_player.remove_rocketparts(item_lost)  # removes the item
                print(f">Time to get a little rest\n\
>As you settle down you notice something in the sky\n\
>Is it... getting closer...??\n\
> You get hit in the head by an asteroid and lose '{item_lost}'")
        elif typeLoss == 2:  # loses money
            money_loss = random.randrange(1500, 2501)  # establishes random amount
            if curr_player.get_curr_money() < money_loss:  # check if the player is able to lose the amount
                curr_player.remove_money(curr_player.get_curr_money())  # removes all of the players money
                print(">As you make you way further you spot some kind of camp\n\
>Before you can react you find yourself surrounded by aliens\n\
>They steal all of your Imperial Credits and disappear into the depths of space")
            else:
                curr_player.remove_money(money_loss)  # removes a random amount of money
                print(f">As you make you way further you spot some kind of camp\n\
>Before you can react you find yourself surrounded by aliens\n\
>They steal {money_loss} Imperial Credits and disappear into the depths of space")
        else:  # loses fuel
            fuel_loss = random.randrange(5, 11)  # set up random amount
            if curr_player.get_curr_fuellevel() < fuel_loss:  # checks if player is able to lose random amount
                curr_player.remove_fuellevel(curr_player.get_curr_fuellevel())  # removes all of the players fuel
                print(">You feel something crawling and nibbling around your pockets\n\
>SPACE PARASITES! They love drinking fuel\n\
>Unfortunately you have lost all of your fuel")
            else:
                curr_player.remove_fuellevel(fuel_loss)  # removes random amount of fuel
                print(f">You feel something crawling and nibbling around your pockets\n\
>SPACE PARASITES! They love drinking fuel\n\
>Unfortunately you have lost {fuel_loss}% of fuel")


def dice_single():
    dice = random.randint(1, 6)
    return dice

def board(curr_player):
    board = ["START", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "11", "12", "13", "14", "15", "16", "17", "18", "19",
             "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
             "31", "32", "33", "34", "35"]

    '''
    # assign functions to positions on the board
    board[0] =  # start payout
    board[2] = board[16] = board[20] = board[25] = board[34] =  # random event
    board[5] = board[7] = board[14] = board[22] = board[32] =  # training field
    board[9] = board[27] =  # pawn shop
    board[11] = board[29] =  # tank stop
    board[18] =  # fallen star
    '''

    step_count = 0
    player_display = curr_player.get_playername()
    player_username = curr_player.get_username()

    while True:
        time.sleep(3)
        print(f"<{colorama.Fore.CYAN}SYSTEM{colorama.Style.RESET_ALL}> It's <{colorama.Fore.YELLOW}{player_username}{colorama.Style.RESET_ALL}> ({colorama.Fore.GREEN}{player_display}{colorama.Style.RESET_ALL}) turn\n")
        print(">ROCKETPARTS:")
        print(curr_player.get_curr_rocketparts_list())
        print(">FUELLEVEL:")
        print(curr_player.get_curr_fuellevel())
        print(">MONEY:")
        print(curr_player.get_curr_money())
        print("")
        time.sleep(3)
        print(f"<{colorama.Fore.CYAN}SYSTEM{colorama.Style.RESET_ALL}> It's <{colorama.Fore.YELLOW}{player_username}{colorama.Style.RESET_ALL}> ({colorama.Fore.GREEN}{player_display}{colorama.Style.RESET_ALL}) turn\n")
        user = input(">Use Enter to roll... ")
        if user == "":
            step_count += dice_single()
            curr_player.move_location((curr_player.get_curr_location() + step_count))
            step_count = curr_player.get_curr_location()

            if step_count >= 36:
                step_count = step_count - 36
                curr_player.move_location(step_count)
                curr_player.add_money(2000)
                print(">Congrats! You have looped around and have been awarded 2000 Imperial Credits")
            board[step_count] = player_display
            print(board[curr_player.get_curr_location(): curr_player.get_curr_location() + 10])
            if player_display == board[0]:
                # call function start
                break
            elif player_display == board[2] or player_display == board[16] or player_display == board[20] \
                    or player_display == board[25] or player_display == board[34]:
                random_event(curr_player)
                break
            elif player_display == board[5] or player_display == board[7] or player_display == board[14] \
                    or player_display == board[22] or player_display == board[32]:
                training_field(curr_player)
                break
            elif player_display == board[9] or player_display == board[27]:
                shop(curr_player)
                break
            elif player_display == board[11] or player_display == board[29]:
                fuelstation(curr_player)
                break
            elif player_display == board[18]:
                fallen_star(curr_player)
                break
            else:
                break
            os.system("cls")
        else:
            print(">Please use Enter!")


def get_rocketparts_amount(curr_player, rocketpart):
    player_collected = curr_player.get_curr_rocketparts_list()
    rocketpart_amount = 0
    for i in player_collected:
        if i == rocketpart:
            rocketpart_amount += 1

    return rocketpart_amount


def buy_rocketpart(curr_player, curr_money, rocketpart, shopkeeper_fullname):
    if curr_money >= 1500:
        curr_player.remove_money(1500)
        curr_player.add_collected(rocketpart)
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> Thanks for the sell! Here are your 1500 Imperial Credits")
    else:
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> You don't have enough Imperial credits to buy this rocketpart")


def sell_rocketpart(curr_player, rocketpart, shopkeeper_fullname):
    curr_gem_amount = get_rocketparts_amount(curr_player, rocketpart)

    if curr_gem_amount >= 1:
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> Thanks for the sell! Here are your 1500 Imperial Credits")
        curr_player.add_money(1500)
        curr_player.remove_rocketparts(rocketpart)
    else:
        print(f"<{colorama.Fore.MAGENTA}{shopkeeper_fullname}{colorama.Style.RESET_ALL}> You don't have enough of this rocketpart to sell")


def ending(player):
    player_username = player.get_username()

    select_space_station = random.randint(0, 19)

    random_number = ""
    while len(random_number) != 5:
        random_int = random.randint(0, 9)
        random_number += str(random_int)

    space_port = f"{colorama.Fore.GREEN}SPACE STATION:{colorama.Fore.BLUE} {dialogue.spaces_station[select_space_station]}{colorama.Fore.GREEN} - COMMUNICATION SYSTEMS - COMMUNICATION POD: {colorama.Fore.CYAN}#{random_number}{colorama.Style.RESET_ALL}"

    underscore = ""
    while len(space_port) != len(underscore):
        underscore += "-"

    print(space_port)
    print(underscore)

    time.sleep(3)
    print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> Congratulations! <{colorama.Fore.YELLOW}{player_username}{colorama.Style.RESET_ALL}>")
    time.sleep(3)
    print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> You have defied the odds and emerged victorious on this adventure")
    time.sleep(3)
    print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> The engines of your newly-built space craft roar to life")
    time.sleep(3)
    print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> You take a final glance at the planet, the trials and tribulations of your journey")
    time.sleep(3)
    print(f"<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> And so you left, in love with a new passion: to explore")
    time.sleep(5)
    print(f"<{colorama.Fore.BLUE}SYSTEM{colorama.Style.RESET_ALL}>  USER:<{colorama.Fore.CYAN}Unknown{colorama.Style.RESET_ALL}> DISCONNECTED FROM COMMUNICATION SYSTEMS")
    time.sleep(5)
    print("THANKS YOU FOR PLAYING OUR GAME")