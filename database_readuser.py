# this will serve as the database, where we will connect to the file system 
# and fetch from the file system

# what we will do in this database
# create a record
# update record
# read record
# delete record 
# all of this is called the CRUD operation
# see how the functions below line up with each CRUD operation 

# we also need to search through the record to find a user

import os
import validation
# this is necessary to delete a file 

user_db_path = 'data/user_record/'

def create(user_account_number, user_details):
    
    user_data = first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(0)

    if does_account_number_exist(user_account_number): # this is checking if the account number already exists 
        return False   

    if does_email_exist(email):
        print('User already exists')
        return False

    completion_state = False # created a variable 

    try: #try block. Here, you are trying to create a file
        f = open(user_db_path + str(user_account_number) + '.txt', 'x')    # That explains all of the components of that line of string 
        # this line is opening a new file (txt file), the name of the file is "account_number" and it's being saved in the user_record folder in the data folder.

    except FileExistsError: # this is one of the errors that can potentially print out if the file already exists 
        does_file_contain_data = read(user_db_path + str(user_account_number) + '.txt', 'x')
        if not does_file_contain_data:
            delete(user_account_number)

        # so then we will delete the already created file and print out error, then return false
        # first we will check the contents of the file before deleting. if there are not contents in the file, then the file will delete 

        #delete(account_number) # this is deleting the file if the user already exists 

    else: # if there are no errors when you create the file, you come here and add the user details
        f.write(str(user_data)) # this is the data you are writing into the file. This is converted into a string because you cannot save a list inside a file. Below when you are calling the function                               
        completion_state = True

    finally: # finally means that anything you write in the try block does not matter, whatever you write in 'finally' will still run
        
        f.close() # this is closing the file that you opened
        return completion_state
        #since everything in finally will always run we put the return statement here instead of at the end of every block of code


    # SECTION SKELETON
    # the plan is to create a file called account_number.txt
    # each time we add a new user, we create a file in a folder 
    # in VS code, tap the "explorer" tab, click the "new folder" icon
    # then the user details are added to the file 
    # return True
    # if saving to file fails, then delete created file. Go to the folder and delete the file with the account number
    # when you run the code again, you will see a new file is created

def read(user_account_number):
    
    # find the user with the account number
    # fetch contents of the file 
    # return True
    
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        
        if(is_valid_account_number):
            f = open(user_db_path + str(user_account_number) + '.txt', 'r') # changed the x from the create function string to r because that is the read parameter
        else:
            f = open(user_db_path + user_account_number, 'r') 

    except FileNotFoundError:
        print('User not found')

    except FileExistsError:
        print("User doesn't exist")

    except TypeError:
        print('Invalid account number format')

    else: # else always comes after the exceptions 
        return f.readline()

    return False 

def update(user_account_number):
    print('update user record')
    # find user with the account number 
    # go into the folder, search to the file name corresponding to the account number
    # once found, we can fetch the contents of the file
    # update the contents of the file
    # then save the file
    # return True

def delete(user_account_number):
    #print('delete user record')

    is_delete_successful = False # a variable to make coding faster 

    if os.path.exists(user_db_path + str(user_account_number) + '.txt'): # this is checking if the user (file) exists in the database
        is_delete_successful = True 

        try: # put a try block here in case the function fails 
            os.remove(user_db_path + str(user_account_number) + '.txt') #if the file does exist then this is where we are calling to delete it 
        except FileNotFoundError: # we ran the code without this try block to see what potential error we would get back and then we added the try block
            print('User not found')

        finally: 
            return is_delete_successful # the variable above 

    # SECTION SKELETON
    # find the user with the account number 
    # delete the user record (file)
    # return True 

def does_email_exist(email): # this requires an arguement, so we're going to find the user based on their account number
    
    all_users = os.listdir(user_db_path) # created a variable here
    # we are going to look through every file in the folder that contains user account numbers

    for user in all_users:
        user_list = str.split(read(user), ',') # this is splitting the account user files so that it is no longer a string
        if email in user_list:
            return True # this means the user email exists 
    return False 

def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path) # created a variable here
    # we are going to look through every file in the folder that contains user account numbers

    for user in all_users: # this is checking if the account number already exists 

        if user == str(account_number) + '.txt':
            return True 
        
    return False 
         
def authenticated_user(account_number, password): #this is checking if the account number exists 

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ',') # this means that we are reading that data that belongs to this account owner and converting it to a list 
        if password == user[3]:
            return user 

    return False 



print(does_account_number_exist(6005439814))
#print(read({'one', 'two'}))
# this is calling the function with the required arguments