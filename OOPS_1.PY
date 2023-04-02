class animal:
    type_="carnivorous"  #class variables

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.food="meat"  #instance variable


    def eat(self):
        return f"{self.name} of {self.age}  only consume milk"
    
    def compare(self,obj1):
        if self.name== obj1.name:
            print("yees its same")

        else:
            print("its not same")


    


cat=animal('cat','2years')
dog=animal('dog','5years')

print(cat.eat())
print(isinstance(cat,animal))
print(cat.type_);
