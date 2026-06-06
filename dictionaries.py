# STORE INFO WHICH COME AS KEY VALUES PAIR LIKE NAME, EMAIL AND PHONE NUMBER

customer = {
    'name': 'Payal', # SEPERATED BY COMMA
    'age' : 30,
    'is_verified': True
}
print(customer['is_verified'])

# IF THERE IS NO SUCH DICTIONERIES THEN ERROR CAME TO PREVENT IT AND GET 'NONE' THUS,
print(customer.get('birthdate'))


