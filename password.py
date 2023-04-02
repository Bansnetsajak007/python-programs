import random

def generate(r,n,s,b,scahr):
    password= b[r]+s[r]+scahr[r]+n[r]+scahr[r]+n[r]+s[r]

    return password
    




numbers_=[i for i in range(1,12)]
small_alphabet=['q','w','e','s','a','m','l','o','t','x','z']
big_alphabet=['Q','W','E','S','A','M','L','O','T','X','Z']

special_char=['!','@','#','$','%','^','&','*','(',')','+']



r= random.randint(1,11)

print("The computer generated password is: \n")
print(generate(r,str(numbers_),small_alphabet,big_alphabet,special_char))

# # for i in small_alphabet:
# #     number=+1
# #     # print(i)

# print(len(special_char))