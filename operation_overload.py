# a=10
# b=30

# print(int.__add__(a,b))

# class add:
#     @classmethod
#     def __ret__(cls,a,b):
#         return(a +b)




# print(add.__ret__(1,3))
 


class student:
    def __init__(self,m1,m2) -> None:
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        a=self.m1 + self.m2
        b=other.m1 +  other.m2

        return ((f"Hari marks is {a} and ramesh mark is {b}"))

    


hari=student(45,30)
ram= student(20,30)

print(hari.__add__(ram


))






