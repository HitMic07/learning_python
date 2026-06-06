# putting dob and then program calc age
# dob = input('birth year: ')
# age = 2026 - dob
# print(age)

# THERE IS GOING TO BE ERROR HERE BECAUSE CODE LOOK LIKE
# 2026 - '2007'(THIS IS STRING)
# YOU CAN SUBTRACT NUMBER AND STRING

# CORRECT CODE:

dob = input('birth year: ')

age= 2026 - int(dob)
print(age)

print(type(dob))
print(type(age))
