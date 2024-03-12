# ---------------------------------------------------------------------------------------
# Project                      : SPACE RACE
# Project collaborators        : Sogaand, Julian, Danny
# Project objective            : Creating a digital board game based in the Terminal
# Project documentation        :
# Last change preformed (Date) : 06/03/2024 12:15
# Last change preformed by     : Danny
# Last change (Description)    : Created the first version of the player class + its required functions
# ---------------------------------------------------------------------------------------

class Player:
    def __init__(self):
        self.username = ""
        self.playername = ""
        self.curr_rocketparts_list = []
        self.curr_fuellevel = 0
        self.curr_money = 0
        self.curr_location = 0
        self.turns_used = 0

    # Add/update/Set functions

    def set_username(self, username):
        self.username = username

    def set_playername(self, playername):
        self.playername = playername

    def add_rocketparts(self, item):
        self.curr_rocketparts_list.append(item)

    def add_fuellevel(self, fuel):
        self.curr_fuellevel += fuel

    def add_money(self, money):
        self.curr_money += money

    def move_location(self, new_location):
        self.curr_location = new_location

    def update_turns_used(self):
        self.turns_used += 1

    # Remove/subtract functions
    def remove_rocketparts(self, item):
        self.curr_rocketparts_list.remove(item)

    def remove_fuellevel(self, fuel):
        self.curr_fuellevel -= fuel

    def remove_money(self, money):
        self.curr_money -= money

    # Data retrieval functions

    def get_username(self):
        return self.username

    def get_playername(self):
        return self.playername

    def get_curr_rocketparts_list(self):
        return self.curr_rocketparts_list

    def get_curr_rocketparts_pos(self, pos):
        return self.curr_rocketparts_list[pos]

    def get_curr_fuellevel(self):
        return self.curr_fuellevel

    def get_curr_money(self):
        return self.curr_money

    def get_curr_location(self):
        return self.curr_location

    def get_turns_used(self):
        return self.turns_used
