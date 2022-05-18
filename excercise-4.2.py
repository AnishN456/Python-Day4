#This program is used to randomly pick the names who will pay for the entire bill.
#First, import the random module.
import random

#get the names of the people who are going to pay as the input.
names=input("Enter the names who aare going to pay the bill:")

#This will convert the string to lists.
names_list=names.split(", ")

#get the length of the list.
number = len(names_list)

#get the random number from the start to end of the list.
i = random.randint(0,number)

#print the person who is going to pay the bill randomly.
print(f"{names_list[i-1]} is going to buy the meal today.")