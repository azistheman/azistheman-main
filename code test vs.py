import logging
import random
x=0
botwon=False
high=10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
low=1
MyNumber= random.randint (low, high)
robotnumber= random.randint(low, high)
print (robotnumber)
while botwon==False:
    if robotnumber>MyNumber:
        print ("lower")
        high=robotnumber-1
        robotnumber= random.randint(low, high)
        x=x+1
        print (robotnumber)
    if robotnumber<MyNumber:
        print ("higher")
        low=robotnumber+1            
        robotnumber=random.randint(low, high)
        x=x+1
        print (robotnumber)
    if robotnumber==MyNumber:
        print ("winner")
        x=x+1
        botwon=True
        print ("number of guesses:", x)
        print ("good robot")