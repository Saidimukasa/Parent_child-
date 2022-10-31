
from Parent import Parent
class Child(Parent):
    def __init__(self,Firstname,lastname,Age,sex):
        Parent.__init__(self,Firstname,lastname,Age,sex)
        self.firstname = Firstname
        self.lastname = lastname
        self.Age = Age
        self.sex = sex
    def Childfull_name(self):
        print(self.firstname,self.lastname)
        
    def printage(self):
        print(self.Age)