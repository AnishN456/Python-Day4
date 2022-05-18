import random

#here the result vriable stores random number 0 or 1
result=random.randint(0,1)

#and then if result=0 then it is tails and if it is 1, then it is heads.
if result==0:
    print("Tails")
else:
    print("Heads")