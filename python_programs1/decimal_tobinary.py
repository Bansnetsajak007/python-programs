# def decimal_to_binary(d_num):
#     rem=[]
#     n=2
#     while True:
#         if d_num%n == 1 or d_num%n==0:
#             rem.append(d_num%n)
#         else:
#             rem.append(d_num%(n+1))

#         if d_num==1:
#             break

#     return rem

# num= int(input("Enter a decimal number: "))

# print(decimal_to_binary(num))

a = 5
#this prints the value of "a" in binary
print(bin(a))