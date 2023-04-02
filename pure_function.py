# a= 12

# def change_a(a,b):
#     c=a
#     a=b
#     return a

# print(a)
# print(change_a(12,24))



li=[1,2,3,4]

def change_list(n,list):
    li_C=li.copy()
    li_C.append(n)
    return li_C


print(li)
print(change_list(5,li))