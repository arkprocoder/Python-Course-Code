# operators Overloading and dunder methods
class Employee:
    no_of_leaves=14

    def __init__(self,aname,asal,arole,anumber):
        self.name=aname
        self.salary=asal
        self.role=arole
        self.phone=anumber

    def printDetails(self):
        return f"Name is {self.name}\nSalary is {self.salary}\role is { self.role}\nNumber is {self.phone}\n"

    @classmethod
    def change_of_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    def __add__(self,other):
        return self.salary+other.salary

    def __truediv__(self,other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employe repr is {self.name}\nSalary is {self.salary}\role is { self.role}\nNumber is {self.phone}\n"

    def __str__(self):
        return f"Employe str is {self.name}\nSalary is {self.salary}\nrole is { self.role}\nNumber is {self.phone}\n"

emp1=Employee("Sai",25000,"developer",7896541230)
emp2=Employee("Ark",5000,"developer",7896541230)
# print(emp1.no_of_leaves)
# print(emp1.change_of_leaves(25))
# print(emp1.no_of_leaves)
# print(emp2.no_of_leaves)
# print(emp1+emp2)
# print(emp1/emp2)
print(emp1)
print(repr(emp2))