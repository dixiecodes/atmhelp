import random
import validation
import database
from getpass import getpass # this must be entered if you don't want the password to be displayed on the screen 

account_number_from_user = None 

def init():
    print("Welcome to bank Python")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n")) # a variable that's printing the statement and allowing integer entries

    if have_account == 1: # if #1 is selected from the variable, initiate the login function 

        login() # calling the login function 

    elif have_account == 2: # if #1 is not selected, and #2 is selected then it will call the register function 

        register() #calling the register function 

    else: # if 1 and 2 are not selected then the print statement below will appear and the init function is called 
        print("You have selected invalid option")
        init()


def login(): # when this function is called it will print the statement below 
    print("********* Login ***********")

    global account_number_from_user # explain this again.....

    account_number_from_user = input("What is your account number? \n") # a variable that's printing the statement and allowing the user to type a response

    is_valid_account_number = validation.account_number_validation(account_number_from_user) # a variable that is importing the validation module and the account_number_validation function 

    if is_valid_account_number: # if the validation import returns true, the comp. will ask for the password but not display it on the screen

        password = getpass("What is your password \n") # a variable that's printing the statement and allowing the user to type a response that will not be displayed (what the getpass is for)

        user = database.authenticated_user(account_number_from_user, password) # a variable that is importing the database module and the authenticated_user function. This is also calling the account number abd the password

        # num. 2 of the HW create a function here that creates a new file that gives me a string that tells us what time the user logged in 

        if user: # if the user types in the correct password then it takes the user to the bankoperation function and opens up the user variable that is importing from the database.py file 
            bank_operation(user)

        print('Invalid account or password') # if user does not enter the right password, this message appears 
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers") # if user does not enter the right account number, this msg appears 
        init()


def register():
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number()

    is_user_created = database.create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("Invalid option selected")
        bank_operation(user)

def withdrawal_operation():
    print('Withdrawal')
    withdraw=input('How much would you like to withdraw? \n')
    print('Take your cash')
    bankoperation2()

def deposit_operation():
    print('This is the {} account number'.format(account_number_from_user))
    print('Deposit Window')

    view_balance = get_current_balance(account_number_from_user)

    deposit_file = database.save_deposit_balance(create, balance)

    print('This is your current balace {}'.format(view_balance))
    
    deposit = input('How much would you like to deposit? \n') 
    print('You selected to deposit %s' % deposit)
    # call the new deposit function from database.py here and pass the account number as an argument 
    # add the deposit to the balance 
    # then set the balance 

    current_balance = int(deposit) + int(view_balance) # this is converting the strings to integers 

    update_balance = set_current_balance(account_number_from_user,current_balance)

    bankoperation2()

def bankoperation2():

    selectedoption = int(input('Would you like to perform another function? (1) Yes (2) No \n'))

    if(selectedoption == 1):
        bankoperation3()

    elif(selectedoption == 2):
        exit() 
    
    else:
        
        print('Invalid option selected')
        logout()

def bankoperation3():
    
    selectedoption2 = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))
    
    if(selectedoption2 == 1):
       
        depositoperation()
    elif(selectedoption2 == 2):
        
        withdrawaloperation() 
    elif(selectedoption2 == 3):
        
        logout() 
    elif(selectedoption2 == 4):
        
        exit()
    else:
        
        print('Invalid option selected')
        bankoperation()


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance): # this updates the balance in the database 
    user_details[4] = balance 


def get_current_balance(user_details):
    return user_details[4]


def logout():
    # for number 3 on the HW call the delete function here
    login()
    


init()