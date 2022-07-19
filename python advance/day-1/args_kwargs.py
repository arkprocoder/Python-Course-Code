
# def funargs(normal,*args):
#     print(type(args))
#     print(normal)
#     for i in args:
#         print(i)


# normal="The sum is  :"

# funargs(normal,1,2,34,5,3,2,1,34,5,56,7)

def func_args_kwarg(title,*args,**kwargs):
    print(title)
    for n in args:
        print(f"The name is {n}")

    print("\n")
    print("\nNow i am printing Kwargs")

    for name,role in kwargs.items():
        print(f"Name is {name}, Role is {role}")


    

print("hey i am starting")
names=["rohan","teju","sachhin"]
title="Python Course"
kw={
    "rohan":"Developer",
    "teju":"Designer",
    "sachhin":"Tester"
}

func_args_kwarg(title,*names,**kw)