# multilevel inheritance
class FirstYear:
    ffriends="aishwarya,harshith,aadithyaa,aneeqah"

class SecondYear(FirstYear):
    sfriends="meghana,amrutha"

class ThirdYear(SecondYear):
    tfriends="akhil, chandan"
    
class FourthYear(ThirdYear):
    fourFriends="AAdithyaa,meghana,harshith,amrutha"

# obj1=SecondYear()
# print(obj1.ffriends)
# print(obj1.sfriends)
obj2=FourthYear()
print(obj2.ffriends)
print(obj2.sfriends)
print(obj2.tfriends)
print(obj2.fourFriends)