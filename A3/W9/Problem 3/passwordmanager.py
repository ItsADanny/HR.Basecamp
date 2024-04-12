# This class will function as our password manager
class PasswordManager:
    # This holds the current password
    curr_password = ""

    # This list holds all the old_passwords
    old_passwords = []

    # This function gets the current password
    def get_password(self):
        return self.curr_password

    # This function sets the current password
    def set_password(self, new_password):
        self.old_passwords += self.curr_password
        self.curr_password = new_password
        return True

    # This function checks if the attempt by the user is the same as the current password
    def is_correct(self, attempt):
        if attempt == self.curr_password:
            return True
        return False
