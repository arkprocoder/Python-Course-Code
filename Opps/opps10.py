from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def mandatory(self):
        return "aa"
 
    @abstractmethod
    def add(self):
        pass

class Circle(Shape):
    def greet():
        print("good Morning")
    
    def mandatory(self):
        return "anees"
    type="Circle"
    Sides=0
    def __init__(self):
        self.radius=5
        self.pi=3.14
    
    def areaCircle(self):
        return self.pi* self.radius* self.radius

    

    def add(self):
        return "anness"  

ob1=Circle()
print(ob1.mandatory())
print(ob1.areaCircle())