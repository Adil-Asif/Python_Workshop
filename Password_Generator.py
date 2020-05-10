import random

char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPPQRSTUVWXYZ123456789-_$£%&~/?|"

length = input("Enter length of password: ")
password = ''

for i in range(0,int(length)):
    password += random.choice(char_set)
print(f"Your Password is generated: {password}")