#Jackson Pike | Flow Chart to Program Practice | Oct 2018
import winsound
gusername = "undefined"
gpassword = "undefined"

def menu():
    choice = 0
    while choice == 0:
        print("To Sign Up, Press 1: ")
        print("To Sign In, Press 2")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            setupUsername = get_username()
            setupPassword = get_password()
            choice = 0
        elif choice == 2:
                usrname_attempt = input("Please Enter Username: ")
                pass_attempt = input("Please Enter Password: ")
                login = check_account(usrname_attempt, pass_attempt)
                return login
        else:
            print("You didn't choose 1 or 2! Try Again")
            menu()


def get_password():
    print("Please create a password. ")
    print("Must Be: 8 Characters long and alphanumeric and contain at least one symbol.")
    passwordSet = input("Enter Password Now: ")
    if len(passwordSet) >=8 and not passwordSet.isalnum():
        global gpassword
        password = passwordSet
        gpassword = password
        return password
    else:
        print("Password did not meet parameters. Try again: ")
        get_password()
def get_username():
    print("Hello! Please create your username: ")
    print("Must Be: Less than 8 Characters Long and it cannot contain special characters")
    usernameSet = input("Enter Your Username: ")
    if len(usernameSet) <= 8 and usernameSet.isalnum():
        global gusername
        username = usernameSet
        gusername = username
        return username
    else:
        print("Username did not meet parameters. Try again: ")
        get_username()
def check_account(usrname, passwrd):
    print(usrname, passwrd, gusername, gpassword)
    if usrname == gusername and passwrd == gpassword:
        return True
    else:
        return False
def successBeep():
    winsound.Beep(700, 2000)
#def deniedBeep():

def main():
    login = False
    login = menu()

    if login == True:
        print("Welcome! You got in.")
        successBeep()
    else:
        print("Sorry, Access Denied!")
main()