#exercise 2 - Faulty Calculator
# 45*3=555 , 56+9=77,56/6=4
#Design a ccalculator which will correctly solve all th problems
#except the following ones:
#input two numbers by the users
#and return the result
a=int(input("Enter the first number"))
op=input("Enter the type of operator")
b=int(input("Enter the second number"))
if(a==45 and b==3):
    print("555")
elif(a==56 and b==9):
    print("77")
elif(a==56 and b==6):
    print("4")
elif(op == "+"):
    print("your ans will be",a+b)
elif(op == "-"):
    print("your ans will be",a-b)
elif(op == "*"):
    print("your ans will be",a*b)
elif(op == "/"):
    print("your ans will be",a/b)


