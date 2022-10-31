# Parent Class
class Parent:
    def __init__(self,Firstname,lastname,Age,sex):
        self.Firstname = Firstname
        self.lastname = lastname
        self.Age= Age
        self.sex = sex  
        #This is the Print name function 
    def Fullname(self):
        print(self.Firstname,self.lastname)   
        # This is the print age function  
    def parentage(self):
        print(self.Age)
    def Action(self):
        return f"I am currently {self.Action}"
    


         