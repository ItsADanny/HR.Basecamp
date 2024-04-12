# This class will function as our password manager
class PasswordManager:
    # This list holds all the old_passwords
    old_passwords = []

    # This function gets the current password
    def get_password(self):
        return self.old_passwords[(len(self.old_passwords) - 1)]

    # This function sets the current password
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            return True
        return False

    # This function checks if the attempt by the user is the same as the current password
    def is_correct(self, attempt):
        if attempt == self.old_passwords[(len(self.old_passwords) - 1)]:
            return True
        return False


if __name__ == "__main__":
    pass
