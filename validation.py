# how this works: it helps to make the code less lengthy. This bloc kof code below was taken
# from the user validation file. it is not put into it's own module and can be imported 
# into the user validation file to decrease the lines of code. 
# see import validation on the module.py file under import random 

def account_number_validation(account_number):

    if account_number is None:
        print('Account cannot be empty')
        return False
    else:
        try: 
            int(account_number) 

            if len(str(account_number)) == 10:
                return True 

        except ValueError:  
            #print('Invalid account number. Account number should be an integer')
            return False  

        except TypeError: 
            #print('Invalid account type')
            return False
        
    #else:
    #    print('Invalid account number, account number must be more or less than 10 digits')
    #    return False