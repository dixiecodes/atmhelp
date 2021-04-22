import random
import os

from getpass import getpass # this must be entered if you don't want the password to be displayed on the screen 

account_number_from_user = None 

user_db_path = "Data/auth_session/"

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

    is_valid_account_number = account_number_validation(account_number_from_user)

    if is_valid_account_number: # if the validation import returns true, the comp. will ask for the password but not display it on the screen

        password = getpass("What is your password \n") # a variable that's printing the statement and allowing the user to type a response that will not be displayed (what the getpass is for)

        user = authenticated_user(account_number_from_user, password) # a variable that is importing the database module and the authenticated_user function. This is also calling the variables from this file (that's within this function)
        #user = str.split(read(account_number_from_user), ',')
        # num. 2 of the HW create a function here that creates a new file that gives me a string that tells us what time the user logged in 

        if user: # if the user types in the correct password then it takes the user to the bankoperation function and opens up the user variable that is importing from the database.py file 
            bank_operation(user)

        print('Invalid account or password') # if user does not enter the right password, this message appears 
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers") # if user does not enter the right account number, this msg appears 
        init()

def does_account_number_exist(account_number_from_user):

    all_users = os.listdir(user_db_path)

    for user in all_users:

        if user == str(account_number_from_user) + ".txt":

            return True

    return False

def authenticated_user(account_number_from_user, password): # is this pulling from the auth.py file? in the register function?

    if does_account_number_exist(account_number_from_user):

        user = str.split(read(account_number_from_user), ',')

        if password == user[3]: 
            return user

    return False

def account_number_validation(account_number_from_user):

    if account_number_from_user:

        try:
            int(account_number_from_user)

            if len(str(account_number_from_user)) == 10: # if the account number is 10 integers long then this function allows the user to proceed to the next step in auth.py
                return True

        except ValueError:
            return False
        except TypeError:
            return False

    return False

def does_email_exist():

    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False

def create(account_number_from_user, first_name, last_name, email, password):

    user_data = first_name + "," + last_name + "," + email + "," + password + ',' + str(0)
    print(account_number_from_user)
    if does_account_number_exist(account_number_from_user):

        return False

    if does_email_exist():
        print("User already exists")
        return False

    completion_state = False

    try: 

        f = open(user_db_path + str(account_number_from_user) + ".txt", "x")

    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(account_number_from_user) + ".txt")
        if not does_file_contain_data:
            delete(account_number_from_user)

    else:

        f.write(str(user_data))
        completion_state = True

    finally:

        f.close()
        return completion_state

def save_deposit_balance(user):

    user_deposit_data = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    print(user_deposit_data)
    
    #create = create()

    try: 

        f = open(user_db_path + str(account_number_from_user) + ".txt", "w")
        f.write(user_deposit_data)
        f.close()

    except FileExistsError:

        does_deposit_file_contain_data = read(user_db_path + str(create) + ".txt")
        pass
        

def save_with_balance():

    user_with_data = first_name + "," + last_name + "," + email + "," + password + current_with_balance

    try: 

        f = open(user_db_path + str(current_with_balance) + ".txt", "x")

    except FileExistsError:

        does_with_file_contain_data = read(user_db_path + str(create) + ".txt")

    else:

        f.write(str(user_data))

    finally:

        f.close()

def read(account_number_from_user):

    is_valid_account_number = account_number_validation(account_number_from_user)

    try:

        if is_valid_account_number:
            f = open(user_db_path + str(account_number_from_user) + ".txt", "r")
        else:
            f = open(user_db_path + account_number_from_user, "r")

    except FileNotFoundError:

        print("User not found")

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account number format")

    else:

        return f.readline()

    return False

def delete():

    is_delete_successful = False

    if os.path.exists(user_db_path + str(account_number_from_user) + ".txt"):

        try:

            os.remove(user_db_path + str(account_number_from_user) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("User not found")

        finally:

            return is_delete_successful

def register(): # this is register function
    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")

    account_number = generation_account_number() # a variable that is calling a function from this file 

    is_user_created = create(account_number, first_name, last_name, email, password) # a variable that is importing the database module and the create function. This is also calling the variables from this file (that's within this function)
    # the key is the account number, with the value after the = sign 

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

        deposit_operation(user)
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
    print('This is the account for {}'.format(account_number_from_user))
    print('Withdrawal Window')

    view_with_balance = get_current_balance(account_number_from_user)

    print('This is your current balace {}'.format(view_with_balance))

    withdraw = input('How much would you like to withdraw? \n')
    print('Take your cash')

    current_with_balance = int(view_with_balance) - int(withdraw) # this is converting the strings to integers 

    print('This is your current balace {}'.format(current_with_balance))

    update_with_balance = save_deposit_balance()

    bankoperation2()

    # 1. create a new file with the account number and store it in another folder (not in auth_session). you can name the variable anything
    # 2. in the deposit function, call the 

def deposit_operation(user):
    print('This is the account for {}'.format(account_number_from_user))
    print('Deposit Window')

    view_deposit_balance = get_current_balance(user)

    print('This is your current balace {}'.format(view_deposit_balance))
    
    deposit = input('How much would you like to deposit? \n') 
    print('You selected to deposit %s' % deposit)
    # call the new deposit function from database.py here and pass the account number as an argument 
    # add the deposit to the balance 
    # then set the balance 

    current_deposit_balance = int(deposit) + int(view_deposit_balance) # this is converting the strings to integers 

    print('This is your current balace {}'.format(current_deposit_balance))

    set_current_balance(user,current_deposit_balance)

    save_deposit_balance(user)
    
    #user = str.split(read(account_number_from_user), ',')

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
    logged_out = delete()
    login()
    


init()