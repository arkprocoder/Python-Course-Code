try:
    pass #run the code
except:
    pass #execute this when try fails
else:
    pass #executes when try block has no errors & except block is not used
finally:
    pass #at any cost this block is going to execute


def Divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Exceptions has not occured")
    finally:
        print("i am pro coder")

Divide(10,0)