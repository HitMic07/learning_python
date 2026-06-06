# A CONTAINER WHICH CONTAIN A CODE WHICH PERFORM A SPECIFIC FUNCTION
# BY DEFAULT ALL FUNCTION IN PYTHON RETURN "NONE"

def greet_user():
# (function_name)
# RESERVED KET WORD IN PYTHON MEANS "DEFINE" THE INTERPRATOR SEE THIS AND GO YEAH LETS DEFINE A FUNCTION.
     print('Hi there')
     print('Welcome aboard!')


greet_user() # CALLING A FUNCTION


# PARAMETERS

def greet_user(lets_go): # "NAME" = ACT AS LOCAL VARIABLE DEFINED INSIDE A FUNCTION
    print(f'Hi {lets_go} ') # TO SELECT ALL THE WORDS IN DIFFERENT LINE = SHIFT + F6
    print('Welcome aboard!')

greet_user('John') # ARGUEMENT IS THE VALUE WE SENT TO THE FUNCTION LIKE "JOHN" AND "MARY"
greet_user('Mary')


# RETURN VALUE

def square(number):
    print(number * number)
   
print(square(5))

