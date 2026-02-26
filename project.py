import sys, random, string, csv
from tabulate import tabulate
from helpers import get_length, get_yes_no, info_given

FILE_NAME = "passwords.csv"
def main():

    while True:
        print("Would you like to (W)rite, (G)enerate or (V)iew password? (Q) exits the program")

        # Asks for correct mode of program, wrong input exits the program
        try:
            mode = input("Select mode: ").strip().lower()
            if not mode in ["w", "g", "v", "q", "d"]:
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
            file_name = save(account, encrypted_password)
            info_given(account, password, encrypted_password, file_name)


        elif mode == "v":
            view_pass()
        
        elif mode == "d":
            decrypt_pass()

        else:
            sys.exit("Program ended by user.")

        out = input("Press any key to continue or \"Q\" to quit: ").lower()
        if out == "q":
            sys.exit("Thank you for using password manager!")


def write_pass():

    print()
    print("~~~~~Write Mode~~~~~")
    print()


    # Taking the inputs
    account = input("Password for account: ")
    password = input("Type password: ")


    return account, password



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


    return account, generated_password

def decrypt_pass():
    print()
    print("~~~~~Decrypt Mode~~~~~")
    print()

    password = input("Type the password to decrypt: ").strip()
    print(f"Decrypted Password: {decrypted_password(password)}")

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

    
    with open(FILE_NAME, "r", encoding="utf-8", newline="") as file:
        items = []
        reader = csv.reader(file)
        for account, password in reader:
            items.append([account,decrypted_password(password)])
        
        headers = ["Account", "Password"]
        print(tabulate(items, headers, tablefmt="heavy_outline"))
    


# Encryption
def caesar_cipher(password):

    encrypted_password = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii + 6293

        encrypted_password += chr(encrypted)

    return encrypted_password


# Decryption
def decrypted_password(password):

    decrypted_pass = ""

    for char in password:

        char_ascii = ord(char)
        encrypted = char_ascii - 6293

        decrypted_pass += chr(encrypted)

    return decrypted_pass


# Saves the given info in desired file
def save(account,password):

    with open(FILE_NAME, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([account,password])

    return FILE_NAME

if __name__ == "__main__":
    main()