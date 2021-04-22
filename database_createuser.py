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

def create(account_number, user_details):
    
    completion_state = False # created a variable 

    try: #try block. Here, you are trying to create a file
        f = open('data/user_record/'+ str(account_number) + '.txt', 'x')    # That explains all of the components of that line of string 
        # this line is opening a new file (txt file), the name of the file is "account_number" and it's being saved in the user_record folder in the data folder.

    except FileExistsError: # this is one of the errors that can potentially print out if the file already exists 
        print('User already exists')
        return completion_state  
        # so then we will delete the already created file and print out error, then return false

    else: # if there are no errors when you create the file, you come here and add the user details
        f.write(str(user_details)) # this is the data you are writing into the file. This is converted into a string because you cannot save a list inside a file. Below when you are calling the function                               
        f.close()
        completion_state = True

    #finally: # finally means that anything you write in the try block does not matter, whatever you write in 'finally' will still run
        #f.close() # this is closing the file that you opened
        #return completion_state

    # SECTION SKELETON
    # the plan is to create a file called account_number.txt
    # each time we add a new user, we create a file in a folder 
    # in VS code, tap the "explorer" tab, click the "new folder" icon
    # then the user details are added to the file 
    # return True
    # if saving to file fails, then delete created file. Go to the folder and delete the file with the account number
    # when you run the code again, you will see a new file is created

def read(user_account_number):
    print('read user record')
    # find the user with the account number
    # fetch contents of the file 
    # return True

def update(user_account_number):
    print('update user record')
    # find user with the account number 
    # go into the folder, search to the file name corresponding to the account number
    # once found, we can fetch the contents of the file
    # update the contents of the file
    # then save the file
    # return True

def delete(user_account_number):
    print('delete user record')
    # find the user with the account number 
    # delete the user record (file)
    # return True 

def find(user_account_number): # this requires an arguement, so we're going to find the user based on their account number
    print('find user')
    # find user record in the data folder 

create(6005439815, ['Dixie', 'Sasu', 'dixie@gmail.com', 'carter', '200']) 
# this is calling the function with the required arguments