
# single level inheritance
class Parent:
    no_of_peoples=4
    def __init__(self,name,role,age):
        self.name=name
        self.role=role
        self.age=age

    def ParentDetails(self):
        return f"Parent name is {self.name}\nRole is {self.role}\nage is {self.age}\n"

    def Greeting(self):
        return f"Good Morning {self.name} your age is {self.age}"

class Child(Parent):
    
    def __init__(self,name,role,age,hobby):
        self.name=name
        self.role=role
        self.age=age
        self.hobby=hobby
    
    def ChildDetails(self):
        return f"Child name is {self.name}\nRole is {self.role}\nage is {self.age}\nHobby is {self.hobby}"

    
    # def Greeting(self):
    #     return f"Good Morning {self.name} your age is {self.age} hobby is {self.hobby}"

mother=Parent("zoya","mother",30)
father=Parent("arhan","father",32)

# obj for the children
child1=Child("sai","son",22,"coding")
child2=Child("anees","son",23,"programming")


# print(mother.ParentDetails())
# print(father.ParentDetails())
# print(father.no_of_peoples)

print(child1.no_of_peoples)
print(child1.Greeting())