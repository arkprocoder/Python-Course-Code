# @property


import inspect


class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@gmail.com"

    def personDetails(self):
        return f"The person is {self.fname} {self.lname}"
    

    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return f"email is not set please use setters to set"
        
        return f"{self.fname}.{self.lname}@gmail.com"

    
    @email.setter
    def email(self,string):
        print("Seeting a property ....")
        names=string.split("@")[0]
       # anees.rehman@gmail.com
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


indian=Person("anees","rehman")
# print(indian.email)
# print(indian.personDetails())
indian.email="ark.procoder@gmail.com"
print(indian.fname)
print(indian.lname)
del indian.email
print(indian.fname)
print(indian.lname)
# print(dir(indian))
# print(id(indian))
print(inspect.getmembers(indian))