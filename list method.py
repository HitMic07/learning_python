# THESE ARE THE OPERATIONS WHICH CAN BE DONE ON LIST

# numbers = [5,6,4,3,4]

# numbers.append(20)
# TO ADD THE NUMBER

# numbers.insert(0,10)
# USE TO INSERT NUMBER AT DESIRED POSITION


# numbers.pop()
# TO REMOVE THE LAST DIGIT OF LIST

# numbers.sort()
# TO MAKE THE LIST IN ASCENDING ORDER

# print(numbers)

# QUESTION:
# TO REMOVE THE DUPLICATES IN A LIST

numbers = [3,4,5,6,7,8,2,3]
numbers.sort()
uniques =[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
















