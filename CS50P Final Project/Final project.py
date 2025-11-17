import sys,random,string

def main():

    try:
        print("Would you like to (W)rite, (G)enerate or (V)iew password? (Q) exits the program")
        mode = input('Select mode:').strip().lower()
        if not mode in ["w","g","v","q"]:
            raise ValueError

    except ValueError:
        sys.exit("Invalid input")
    #print(mode)

    if mode == "w":
        write_pass()
    elif mode == "g":
        generate_pass()
    elif mode == "v":
        view_pass()
    else:
        sys.exit("Program ended by user.")

def write_pass():
    print("Write Mode")

    # Taking the inputs
    account = input("Password for account: ")
    password = input("Type password: ")

    # Printing what we wrote
    print(f"Account: {account}")
    print(f"Password: {password}")

    # Generating a csv file with desired name
    file = input("(Without extensions) Select file name to save password: ")
    file = file.replace(".", "") + ".csv"
    #print(file)

    # Calling save to save the file
    save(account,password,file)


def generate_pass():
    print("Generate Mode")

    length = int(input("What should be the length of your password? "))
    numbers = input("Password should include numbers(Y/N)? ")
    specials = input("Password should include special characters(Y/N)? ")



def view_pass():
    print("View Mode")
def save(account,password,file):
    ...
if __name__ == "__main__":
    main()