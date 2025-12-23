'''1 for snake
-1 for water
0 for gun '''
import random

computer = random.choice([1,-1,0])

userstr = (input("enter your choice (s/w/g):"))
userdict = {"s":1,"w":-1,"g":0}

reversedict = {1:"s",-1:"w",0:"g"}

you= userdict[userstr]

print(f"your choice is {reversedict[you]}, and computer choice is {reversedict[computer]}")

if(computer==you):
   print("it's a draw")
else:
    if (computer==1 and you==-1):
        print("you lose")
    elif(computer==-1 and you==0):
        print("you lose")
    elif(computer==0 and you==1):
        print("you lose")
    elif(computer==-1 and you==1):
        print("you win")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==0 and you==-1):
        print("you win")