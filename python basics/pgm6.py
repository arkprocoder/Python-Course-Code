# Taking input from the user
# 1.write a program to take a user first name user last name and user salary,user age and print the details.

# firstName=input("Enter Your first name : \n")
# lastName=input("Enter Your last name: \n")
# age=int(input("Enter Your Age :\n"))
# salary=int(input("Enter Your Salary :\n"))
# print(firstName,lastName,age,salary)
# print(type(firstName),type(lastName),type(age),type(salary))

# 2. Add two numbers taking the input

# num1=input("Enter the first num:\n")
# num2=input("Enter the second num:\n")
# res=int(num1)+int(num2)
# print("result of two number is ", res)

# write palindrome program to validate strings and numbers or anything

pali=input("Enter the number or string or number + string \n") 
if(pali==pali[::-1]):
    print("It is palindrome")

else:
    print("It is not a palindrome")


