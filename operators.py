# def cube(a):
#     result=(a*a*a)
#     print(result)
import operators
import math
import trig


if  operators == "cube":
    number= eval(input("enter number:"))
    x=operators.cube(number)
    print(x)
elif operators =="sin":
    angle = eval (input("enter angle in degrees:"))    
    sin_of_angle= trig.get_sine(angle)
    print(sin_of_angle)
elif operators =="tan":
    angle =eval (input("enter angle in dwegrees:"))
    print (trig.get_tan(angle))    
elif operators=="cos":
    angle=eval(input("enter angle in degrees:"))
    print(trig.get_cos(angle))
else:    
    num1 = eval(input("enter number 1:"))
    num2 =eval(input("enter number 2:"))
    operator=(input("enter operator:"))
          
          
if operator == "+":          
    operator.add(num1,num2 )
  
elif operator == "-": 
    x= operator.substract(num1,num2)   
    print(x)
elif operator=="/":
    x= operator.divide(num1,num2)
    print(x)
elif operator == "*" or "X" or "x":
    x=operator.multiply(num1,num2)
    print(x)


   