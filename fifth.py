a= input("enter any number ")
b= input("enter any number ")

try:
    a=int(a)
    b=int(b)
    sum=a+b

except Exception as e:
    print(e)


print(sum)

