#  Write a class called Password_manager. The class should have a list called 
# old_passwords that holds all of the user’s past passwords. The last item of the list is 
# the user’s current password. There should be a method called get_password that 
# returns the current password and a method called set_password that sets the user’s 
# password. The set_password method should only change the password if the 
# attempted password is different from all the user’s past passwords. Finally, create a 
# method called is_correct that receives a string and returns a boolean True or False 
# depending on whether the string is equal to the current password or not. 

class Password_manager:
    def __init__(self, initial_password):
        # old_passwords holds all passwords, with the current one at the end.
        self.old_passwords = [initial_password]

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):
        """
        The method checks if the new_password exists in the history of old passwords.
        If it's unique, it's added to the list and becomes the new current password.
        If it has been used before, the password remains unchanged.
        """

        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("\nPassword updated successfully.")
        else:
            print("\nPassword has been used before. Please choose a different one.")

    def is_correct(self, password_attempt):
        # bool: True if the string matches the current password, False otherwise.
        return password_attempt == self.get_password()

if __name__ == "__main__":    
    start_password = input("Please create an initial password: ")
    user_account = Password_manager(start_password)
    print("Account created successfully!")

    while True:
        print("\n--- Password Manager Menu ---")
        print("1. Set a new password")
        print("2. Check your password")
        print("3. View current password (hidden)")
        print("4. View password history")
        print("5. Exit")
        
        choice = input("Please select an option (1-5): ")

        if choice == '1':
            new_pass = input("Enter your new password: ")
            user_account.set_password(new_pass)
        
        elif choice == '2':
            attempt = input("Enter the password you want to check: ")
            if user_account.is_correct(attempt):
                print("\nCorrect! That is your current password.")
            else:
                print("\nIncorrect password.")

        elif choice == '3':
            print(f"\nYour current password is: {user_account.get_password()}")

        elif choice == '4':
            print(f"\nYour password history is: {user_account.old_passwords}")

        elif choice == '5':
            print("\nExiting Password Manager. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

