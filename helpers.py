# Helper for generator, password length
def get_length():
    while True:
        try:
            length = int(input("What should be the length of your pass? "))
            if length <= 0:
                print("please enter a valid non-negative number")
            else:
                return length
        except ValueError:
            print("please enter a number")

# Helper for generator, password add no. and specials
def get_yes_no():
    while True:

        choice = input("(Y/N)? ").strip().lower()

        if choice == "y":
            return True

        elif choice == "n":
            return False

        else:
            print("please type \"Y\" or \"N\"")


# Shows all info given
def info_given(account, password, encrypted_password, file_name):

    print()
    print("====================================")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Account      : {account}")
    print(f"Password     : {password}")
    print(f"Encrypted to : {encrypted_password}")
    print(f"Saved to     : {file_name}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("====================================")
    print()