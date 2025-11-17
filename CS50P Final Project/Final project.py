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
    print()
    print("~~~~~Write Mode~~~~~")
    print()

    # Taking the inputs
    account = input("Password for account: ")
    password = input("Type password: ")

    # Printing what we wrote
    print()
    print("~~~~~~~~~~~~~~~~~~~~~")
    print(f"Account: {account}")
    print(f"Password: {password}")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print()


    # Calling save to save the file
    save(account,password)






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

def get_yes_no():
    while True:

        choice = input("(Y/N)? ").strip().lower()

        if choice == "y":
            return True

        elif choice == "n":
            return False

        else:
            print("please type \"Y\" or \"N\"")


def generate_pass():
    print()
    print("~~~~~Generate Mode~~~~~")
    print()

    account = input("Password for account: ")

    #Password generation info
    length = get_length()
    print("Password should include numbers?", end = "")
    numbers = get_yes_no()
    print("Password should include special characters", end = "")
    specials = get_yes_no()
    #print(f"length: {length}, numbers: {numbers}, specials: {specials}")



    #What we generate the password from
    chars = string.ascii_letters
    if numbers:
        chars = chars + string.digits
    if specials:
        chars = chars + string.punctuation
    chars = list(chars)
    random.shuffle(chars)



    #Generating the password
    generated_password = ""
    randomnum = ""
    for _ in range(length):
        n = random.randint(0,len(chars)-1)
        generated_password += chars[n]
        #randomnum += str(n) + ","

    #print(chars)
    #print(randomnum)
    #print(generated_password)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~")
    print(f"Account: {account}")
    print(f"Password: {generated_password}")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print()






def view_pass():
    print()
    print("~~~~~View Mode~~~~~")
    print()

def save(account,password):
    ...
if __name__ == "__main__":
    main()