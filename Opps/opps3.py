class Employee:
    greet="Good Morning\n"

    #calling constructor
    def __init__(self,name,company,sal,role):
        self.name=name
        self.company=company
        self.salary=sal
        self.role=role
    #method


    def EmployeeDetails(self):
        print(f"{self.greet}Name is {self.name}\nCompany is {self.company}\nSalary is {self.salary}\nRole is {self.role} ")
 

    @classmethod
    def change_greet(cls,newgreet):
        cls.greet=newgreet

    @staticmethod
    def CompanyData():
        return f"Total Employees are 1547896"



emp1=Employee("farhana","Amazon","12lpa","cloud")
emp2=Employee("anees","Infosys","5lpa","developer")

# print(emp1.company)
# print(emp2.company)
# emp1.EmployeeDetails()
# print("\n")
# emp2.EmployeeDetails()
# emp2.company="T.C.S"
# emp2.change_greet("\nGood Night")
# emp2.EmployeeDetails()

a=emp1.CompanyData()
print(a)