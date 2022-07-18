
def funargs(normal,*args):
    print(type(args))
    print(normal)
    for i in args:
        print(i)


normal="The sum is  :"

funargs(normal,1,2,34,5,3,2,1,34,5,56,7)