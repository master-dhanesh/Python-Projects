import random

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_,.?0123456789'

quantity = int(input("Quantity of Passwords: "))
length = int(input("Length of Passwords: "))

print('Here are your passwords:')

for pwd in range(quantity):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)

# How can we make password of given string