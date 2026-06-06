# WHEN WE WANT TO COMPARE VALUE WITH VARIABLE

temp = 8

if temp > 28:
    print('Its a hot day')
else:
    print('Its a cold day ')

# "==" = QUALITY OPERATOR

# QUESTION:
## IF NAME IS LESS THAN 3 CHAR LONG
# PRINT 'NAME MUST BE ATLEAST 3 CHAR'
# OTHERWISE IF ITS MORE THAN 50 CHAR LONG
# PRINT 'NAME MUST BE OF MAXIMUM OF 50 CHAR'
Name = 'Omkar'

if len(Name) < 3:
    print('Name must be at least 3 char')
elif len(Name) > 50:
    print('Name must be max of 50 char')
else:
    print('Name looks good')