#super class
class students:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def grade(self):
        return (f"{self.name} has good grades")
        

#sub class
class MAjor_subjects(students):
    def __init__(self,name,subject,rollno):
        self.subject=subject
        super().__init__(name,rollno)  #calls constructor of the base classs

    def display(self):
        return (f"{self.name} the rollno. of {self.rollno} is {self.subject} student")


sajak=MAjor_subjects("sajak","C.S",27)
print(sajak.display())
# hari=MAjor_subjects("hari","C.S")
# sita=MAjor_subjects("sita","History")
sajak=students("sajak",27)
print(sajak.grade())