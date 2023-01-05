class Calci:
    a=int(input("Enter Number:"))
    b=int(input("Enter Another Number:"))
    def Add(self):
        print("The Addition of numbers is: ",self.a+self.b)
    def Sub(self):
        print("The Subtraction of numbers is: ",self.a-self.b)
    def Multi(self):
        print("The Multiplacition of numbers is: ",self.a*self.b)
    def Div(self):
        print("The Division of numbers is: ",self.a/self.b)
emp=Calci()
emp.Add()
emp.Sub()
emp.Multi()
emp.Div()
