class A:
    name="sajak "
    def __init__(self):
        print("this is init of A")
   
    def feature(self):
        return "This is the greatest feature"


    
class B:
    def __init__(self):
        print("this is  init of B")

class C(A,B):
    def __init__(self):
        super().feature()
        print("this is the init of C")
    

obj=C()

print(obj.feature())
print(obj.name)
