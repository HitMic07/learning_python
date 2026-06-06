from builtins import max

# name = ['john','bob','mosh']
# name[0]= ('jon')
# print(name[:])

# FIND THE LARGEST NUMBER IN A LIST

numbers = ['2','5','947','93']
max = numbers[0]
# ASSUMING THAT THE FIRST NUMBER IS LARGEST
for number in numbers:
    if number > max:
        max = number
print(max)
