# List Comprehension
# list1=[]
# for i in range(11):
#     if i%2==0:
#         list1.append(i)

# print(list1)

# list1=[i for i in range(11) if i%2==0]
# print(list1)


# set comprehensions
# alphbhet= {a for a in ["a","b","c"] if a=="c"}
# print(alphbhet)

# dict comprehensions
# Normaldictory = {
#   0 : "name 0",
#   1 : "name 1",
#   2 : "name 2",
#   3 : "name 3",
#   4 : "name 4",
# }
# print(Normaldictory)


# dicComprenhension= {i:f"Name {i}" for i in range(0,100) if i%5==0}
# print(dicComprenhension)

# generators

# def generator(n):
#   for i in range(n):
#     yield i

# a=generator(5)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print("aaa")
# print(a.__next__())