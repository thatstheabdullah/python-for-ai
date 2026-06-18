class Animal:
    def __init__(self ,name,age):
        self.name=name
        self.age=age
        self.aura=0
    
    def mogger(self,age):
        if age>18:
            print("Your a Mogger")
        else:
            print("Your Not a Mgger")
            
    def checkPussy(self,nam):
            if nam=="cat":
                print ("You have a pussy")
            else:
                print("You dont have a pussy")
        
    
                
class Dog(Animal):
        def __init__(self,name,age):
            self.n=name
            self.a=age
            
class Cat(Animal):
        def __init__(self,name,age):
            self.n=name
            self.a=age
    
    
german_shepherd=Dog("Sins",45)
print(german_shepherd.checkPussy(german_shepherd.n))
persian_cat=Cat("cat",4)
print(persian_cat.checkPussy(persian_cat.n))
print(german_shepherd.mogger(german_shepherd.a))
print(persian_cat.mogger(persian_cat.a))


    