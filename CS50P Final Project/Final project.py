import sys,random,string,csv
from tabulate import tabulate

def main():

    try:
        print("Would you like to (W)rite, (G)enerate or (V)iew password? (Q) exits the program")
        mode = input("Select mode: ").strip().lower()
        if not mode in ["w","g","v","q"]:
            raise ValueError

    except ValueError:
        sys.exit("Invalid input")
    #print(mode)

    if mode == "w":

        account, password = write_pass()
        encrypted_password = caesar_cipher(password)
        save(account, encrypted_password)

        """
        decrypted = decrypted_password(encrypted_password)
        print(f"Account: {account}, Pass: {password}, Encrypted Pass: {encrypted_password}, Decrypted Password: {decrypted}")
        """
    elif mode == "g":
        account, password = generate_pass()
        encrypted_password = caesar_cipher(password)
        save(account,encrypted_password)
        """
        decrypted = decrypted_password(encrypted_password)
        print( f"Account: {account}, Pass: {password}, Encrypted Pass: {encrypted_password}, Decrypted Password: {decrypted}")
        """
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

    """
    # Printing what we wrote
    print()
    print("~~~~~~~~~~~~~~~~~~~~~")
    print(f"Account: {account}")
    print(f"Password: {password}")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print()
    """

    # Calling save to save the file
    return account,password




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
    #randomnum = ""
    for _ in range(length):
        n = random.randint(0,len(chars)-1)
        generated_password += chars[n]
        #randomnum += str(n) + ","


    """
    #print(chars)
    #print(randomnum)
    #print(generated_password)
    print()
    print("~~~~~~~~~~~~~~~~~~~~~")
    print(f"Account: {account}")
    print(f"Password: {generated_password}")
    print("~~~~~~~~~~~~~~~~~~~~~")
    print()
    """

    return account,generated_password




def caesar_cipher(password):

    encrypted_password = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii + 6293

        encrypted_password += chr(encrypted)

    return encrypted_password



def decrypted_password(password):

    decrypted_password = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii - 6293

        decrypted_password += chr(encrypted)

    return decrypted_password



def view_pass():
    print()
    print("~~~~~View Mode~~~~~")
    print()

    print("Please type the master password: ", end = "")
    attempts = 3

    while attempts != 0:
        master_password = input().strip()

        if master_password != "6293":
            attempts -= 1
            print(f"Wrong Password! {attempts} attempt(s) remaining!")
        else:
            break

    if attempts == 0:
        sys.exit("Too many wrong attempts! Maybe you are an impostor!")



    print("Would you like to (D)ecrypt a password or (V)iew a file?")
    while True:
        choice = input("(D/V)? ").strip().lower()

        if choice == "d":
            password = input("Type the password to decrypt: ").strip()
            print(f"Decrypted Password: {decrypted_password(password)}")
            break
        elif choice == "v":
            while True:
                file_name = input("Please input file name(with extensions):")
                try:
                    with open(file_name, "r", encoding="utf-8", newline="") as file:
                        file = csv.reader(file)
                        headers = ["Account", "Password"]
                        print(tabulate(file, headers, tablefmt="grid"))
                        break
                except FileNotFoundError:
                    print("File was not found.")
            break
        else:
            print("please type (D) or (V)")







def save(account,password):

    file_name = input("(Without extensions) Select file name to save password: ")
    file_name = file_name.replace(".", "") + ".csv"

    with open(file_name, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account,password])


if __name__ == "__main__":
    main()