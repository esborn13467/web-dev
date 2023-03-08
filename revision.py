from random import randint
player=input("enter_username:")
print ("hello"+player+"!")
counter=0
randomnumber=randint(10,20)
while counter<3 :
    user_number=eval(input("enter a number "))
    counter+=1

    if user_number<randomnumber:
        print("your guess is too low")
    elif user_number>randomnumber:
        print("your guess is too high")

    
        break
    


if user_number==randomnumber:
    print("game over you win")
    
else :
    print("you lose and the number is .........")
    print(randomnumber)


