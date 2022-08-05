# # daimond problem
# class A:
#     def daimondA(self):
#         print("Daimond A")
# class B(A):
#     def daimondB(self):
#         print("Daimond B")
# class C:
#     pass

# class D(B,C):
#     def daimond(self):
#         print("Daimond D")


# a=A()
# b=B()
# d=D()
# # print(a.daimondA())
# # print(b.daimondB())
# d.daimondB()
# d.daimond()
# d.daimondA()

class Class1:
    def m(self):
        print("In Class1") 
        
class Class2(Class1):
    
    def m(self):        
         print("In Class2")    
  
class Class3(Class1):
    def m(self):
        print("In Class3")    
       
class Class4(Class2, Class3):
    pass       
    def m(self):
         print("In Class4")    
  
obj = Class4()
obj.m()