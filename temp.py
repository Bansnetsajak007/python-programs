
num1=input("enter first number: ")
num2=input("enter second number: ")
num3=0

try:
    num3=int(num1)/int(num2)
    print(num3)
        

except Exception as e:
    print(e,"something went wrong!")

except ZeroDivisionError as e:
    print(e)
        




    
