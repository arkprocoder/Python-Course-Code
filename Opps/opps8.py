# Super method and Overriding methods
class A:
    message="Hello dude how are you am fine sai it is class A"
    def __init__(self):
        self.title="Class A title"
        # self.Instance="Class A Instance"

    
class B(A):
    message="Hello sai it is Class B"
    def __init__(self):
        self.title="Class B title"
        self.Instance="Class B Instance"
        super().__init__()

a=A()
b=B()
# print(a.title)
# print(a.Instance)
# print(b.title)
# print(b.Instance)
# print(a.message)
# print(b.message)
print(b.Instance)