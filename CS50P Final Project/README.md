# Encrypted Password Manager
#### Video Demo:  https://youtu.be/M-CXeXUXFhA


### Description: 
The program is a secure command-line interface password manager. The aim of this 
program was to remove all frustration related to storing passwords and remembering
passwords for all sorts of sites. It also helps to generate strong unique
passwords as per the user's request. All the passwords the user types are stored
in a csv file as per the user's choice, the passwords in the csv file are encrypted,
so even if someone gets access to the csv file, they won't be able to decipher anything.

### Features:

The program comes with **3** modes: **Write**, **Generate**, **View**

When the program is started, if anything other than **W**, **G**, **V** or **Q** is passed
to input, the program closes. This was a design choice because I wanted the user to be 
fully attentive when proceeding to the next steps as there is no way in the program 
to modify the given inputs i.e. accounts, password and file name.


#### Write Mode

This is the simplest mode of the program. When initiated with **"W"** the program
prompts the user to type an account followed by password. The password then goes
to the caesar_cipher function to be encrypted. It returns the encrypted password.
Then the user is prompted to give a file name without extensions. This was a design choice
as well because I wanted to create a csv file no matter the input. If the user still types
the extension the "." is replaced and a csv vile is created anyway. Finally the info_given
function is called where it displays the account, password, encrypted password and the
file it was saved to.


#### Generate Mode

Similar to write mode when initiated with **"G"** the program prompts the user to type 
an account. Then the user is prompted to type a non-negative integer, this part is a
bit forgiving as it keeps prompting the user until a valid number is given. Next the
user is asked if they want numbers and/or special characters in their password 
respectively. Based on these inputs with the help of Python's random and string 
libraries cryptographically strong passwords are generated. Then the program follows the
same procedure as the Write Mode.

#### View Mode

hen initiated with **"V"** the program prompts the user to type the master password which
is hard coded to 6293. The user gets 3 tries to get it right, otherwise the program closes.
If however they type the correct master key. They are presented with 2 further choices:
Decrypt or View file. This is also a forgiving process as it keeps prompting the user
to type D or V. 

If the user types D the program asks for the encrypted password as input and
gives the decrypted password as output.

If the user types V the program asks for the file name, if file is not found it raises an 
error and asks the user again. When correct file name is given the program displays the 
contents of the csv file decrypted with the help of tabulate library.
