
class students:
    school="Adams"

    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2= m2
        self.m3= m3

    def avg(self):
        return((self.m1+self.m2+self.m3)/3)

    def get_m1(self):
        return(self.m1)

    def put_m1(self,marks):
       self.m1=marks
       return(f"marks changed to {marks}")

    @classmethod
    def calss_info(cls):
        return cls.school

    @staticmethod
    def Static_method():
        return "This is a static method it has nothing to do with instance,class variables and method"


# students.school="banset"


sajak= students(56,63,56)
hari=students(78,66,90)

# print(sajak.put_m1(10))
# print(sajak.get_m1())
# print(hari.Static_method())
print(students.calss_info())  # returns adams
        