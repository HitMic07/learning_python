# INPUT WEIGHT AND THEN ASK WHETHER ITS IN LBS OR KILO AND THEN CONVERT IT

weight = input('Weight = ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
   converted =  int(weight) * 0.45
elif unit.upper() == "K":
   converted =  int(weight)/ 0.45

print(converted)



