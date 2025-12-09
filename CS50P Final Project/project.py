import sys,random,string,csv
from tabulate import tabulate

def main():

    print("Would you like to (W)rite, (G)enerate or (V)iew password? (Q) exits the program")

    # Asks for correct mode of program, wrong input exits the program
    try:
        mode = input("Select mode: ").strip().lower()
        if not mode in ["w","g","v","q"]:
            raise ValueError

    except ValueError:
        sys.exit("Invalid input")


    # Program goes to different modes as per user input
    if mode == "w":

        account, password = write_pass()
        encrypted_password = caesar_cipher(password)
        file_name = save(account, encrypted_password)
        info_given(account, password, encrypted_password, file_name)


    elif mode == "g":

        account, password = generate_pass()
        encrypted_password = caesar_cipher(password)
        file_name = save(account,encrypted_password)
        info_given(account, password, encrypted_password, file_name)


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


    return account,password



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



    #Passwoed generation customization as per user input
    chars = string.ascii_letters
    if numbers:
        chars = chars + string.digits
    if specials:
        chars = chars + string.punctuation
    chars = list(chars)
    random.shuffle(chars)



    #Generating the password
    generated_password = ""
    #randomnum = ""
    for _ in range(length):
        n = random.randint(0,len(chars)-1)
        generated_password += chars[n]
        #randomnum += str(n) + ","


    return account,generated_password


def view_pass():
    print()
    print("~~~~~View Mode~~~~~")
    print()


    # Type password to be able to view file
    print("Please type the master password: ", end="")

    attempts = 3
    while attempts != 0:
        master_password = input().strip()

        if master_password != "6293":
            attempts -= 1
            print(f"Wrong Password! {attempts} attempt(s) remaining!")
        else:
            break
    if attempts == 0: # After 3 attempts file stops
        sys.exit("Too many wrong attempts! Maybe you are an impostor!")



    # View a whole file or just decrypt 1 password
    print("Would you like to (D)ecrypt a password or (V)iew a file?")
    while True:
        choice = input("(D/V)? ").strip().lower()


        # Prints the password given decrypted, program ends after execution
        if choice == "d":
            password = input("Type the password to decrypt: ").strip()
            print(f"Decrypted Password: {decrypted_password(password)}")
            break


        # Prints the file in a table with all passwords decrypted, program ends after execution
        elif choice == "v":
            while True:
                file_name = input("Please input file name(without extensions): ")
                file_name = file_name + ".csv"

                try:
                    items = []
                    with open(file_name, "r", encoding="utf-8", newline="") as file:

                        reader = csv.reader(file)
                        for account,password in reader:
                            items.append([account,decrypted_password(password)])

                        headers = ["Account", "Password"]
                        print(tabulate(items, headers, tablefmt="heavy_outline"))
                        break
                except FileNotFoundError: #Keeps asking for file if not found
                    print("File was not found.")
            break


        # Keeps asking user to type correct version
        else:
            print("please type (D) or (V)")
    stop()



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


# Encrypts the password
def caesar_cipher(password):

    encrypted_password = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii + 6293

        encrypted_password += chr(encrypted)

    return encrypted_password

# Decrypts the password
def decrypted_password(password):

    decrypted_pass = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii - 6293

        decrypted_pass += chr(encrypted)

    return decrypted_pass


# Saves the given info in desired file
def save(account,password):

    file_name = input("(Without extensions) Select file name to save password: ")
    file_name = file_name.replace(".", "") + ".csv"

    with open(file_name, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account,password])

    return file_name

# Shows the info provided and program ends
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
    stop()

def stop():

    while True:
        exit_program = input("Press Q to exit program: ").lower()
        if exit_program == "q":
            break
    sys.exit()



if __name__ == "__main__":
    main()