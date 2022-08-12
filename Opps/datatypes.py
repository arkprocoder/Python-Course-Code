class Family:
    no_of_peoples=5 #public
    _siblings=3 #protected
    __son=1 #private

ob1=Family()
print(ob1.no_of_peoples)
print(ob1._siblings)
print(ob1._Family__son)
