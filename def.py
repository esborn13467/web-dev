# def add(num1,num2):
#       result=num1+num2
#       print(result)
# def subtract(num1,num2)
#     result=num1-num2
#     print(result)
# def multiply(num1,num2)
#   result=num1+num2 
# print(result) 
number1=eval(input("enter first number"))
number2=eval(input("enter second number"))
operator=input("enter operator(+,-,/,*):")
 
if operator =="+":
      add(number1,number2)
elif operator=="-":
     subtract(number1,number2) 
elif operator=="/":
    divide(number1,number2)
elif operator=="X"or operator=="x"or operator=="*":
 multiply(number1,number2)
else:
 print("invalid operator")

 


