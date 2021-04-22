import random # this is to generate the bank number, it's connected to the "random" code
import validation # see validation.py file for explanation. This was taken from this file and made into a module to reduce the lines of code. It should work the same way the uservalidation/py file works
import database_readuser
from getpass import getpass  

database = {      # this is a dictionary 
    6005439815: ['Dixie', 'Sasu', 'dixie@gmail.com', 'carter', '200']
} 
# this library database will be replaced with a file system. So that when a new user registers there will be a file of account numbers
# see the import database code 

def init(): # init is short for initializing 
    
    print('Welcome to Bank Python') # FIRST STOP FOR USER (string)

    haveaccount = int(input('Do you have an account with us? 1(Yes) 2 (No) \n')) # SECOND STOP FOR USER (string)
    
    if(haveaccount == 1): # if they select 1
        
        login() # this calling the function
    elif(haveaccount == 2): # The elif keyword = "if the previous conditions were not true, then try this condition"

        register() # this calling the function. the ATM will print this function 
    else: # The else keyword catches anything which isn't caught by the preceding conditions.
        print('You have selected an invalid option') # this will display if they do not select 1 or 2
        init() # if all this fails and it gets to else, then it initializes the application all over again    
   
   #this ends the initializing section 

def login(): # this is creating the function which will appear after you create an account
    print('===== LOGIN =====')

    account_number_from_user = input('What is your account number? \n') 

    is_valid_account_number = validation.account_number_validation(account_number_from_user) #this is sending the account number the user enters to the "account_number_validation" below
   
    if is_valid_account_number:
    
        #password = input('What is your password? \n')
        password = getpass('What is your password? \n')
        # this allows the user to type hte password without it showing on the screen 

        user = database_readuser.authenticated_user(account_number_from_user, password)

        if user:
            bankoperation(user) 

        #for account_number,user_details in database.items(): #for loop 
            #if account_number == int(user_account_number): #since we are no longer converting the integer when you input the account number (remember you took "int" out), we now have to convert it here
                #if(user_details[3] == password):
                    #bankoperation(user_details) # this is calling the bank operation function

        print('Invalid account or password')
        login() #this function tells the computer to start over at login if it gets to this print statement
    
    else:
        print('Account number invalid. Check that you have no more or less than 10 integers')
        init()
    
def register(): # this is creating the function
    print('=====Register======')

    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    #password = input('Create a password \n')
    password = getpass('Create a password \n')
    # the code above in the "register" section is colelcting information from ther user

    account_number = generateanaccountnumber() # this is a function created 
    #prepared_user_details = first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(0)
    
    is_user_created = database_readuser.create(account_number, first_name, last_name, email, password)


    #database[account_number] = [first_name, last_name, email, password, 0] # this is for the dictionary
    #then this information from "register" is then saved in the dictionary 
    # for this dictionary module file, we will use a module to create new user records

    if is_user_created:

        print('Your account has been created!')
        print('==== ==== ====== ====')
        print('Your account number is: %d' % account_number)
        print('Make sure you keep it safe!')
        print('==== ==== ====== ====')

        login() # this is calling the login function 
    else:
        print('Something went wrong, please try again')
        register()
    #print('This is the register function')

def bankoperation(user):

    print('Welcome %s %s!' % ( user[0], user [1] ) )

    selectedoption = int(input('What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))
    
    if(selectedoption == 1):
       
        depositoperation()
    elif(selectedoption == 2):
        
        withdrawaloperation() 
    elif(selectedoption == 3):
        
        logout() 
    elif(selectedoption == 4):
        
        exit()
    else:
        
        print('Invalid option selected')
        bankoperation(user)

def withdrawaloperation():
    print('Withdrawal')
    withdraw=input('How much would you like to withdraw? \n')
    print('Take your cash')
    bankoperation2()

def depositoperation():
    print('Deposit')
    deposit=input('How much would you like to deposit? \n') 
    print('You selected to deposit %s' % deposit)
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

def generateanaccountnumber(): #this is calling the function that was created
    #print('Generating account number...')
    return random.randrange(1111111111,9999999999) # the return is connected to the "import" code

def logout():
    login() # this will take you back to the login page 

#print(generateanaccountnumber()) # this is calling the function that was created

init() # this is calling the function that was created