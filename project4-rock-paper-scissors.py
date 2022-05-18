import random
#Here rock, paper and scissors variables are the ascii art for rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Here choice is the input to choose rock, paper and scissors for the player.
choice = int(input("what do you choose? 0 for rock, 1 for paper and 2 for scissors:"))
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
elif choice==2:
    print(scissors)
else:
    print("No, you cannot enter the valus greater than 2.")
    exit()
    
#Here computer_choice is the input where the computer chooses rock paper or scissors randomly.
print("Computer Chooses:\n")
computer_choice=random.randint(0,2)
if computer_choice==0:
    print(rock)
elif computer_choice==1:
    print(paper)
else:
    print(scissors)
 
#Winning condition for paper to win.
if choice==0 and computer_choice==1:
    print("Computer wins")
elif choice==1 and computer_choice==0:
    print("You win")

#Wining condition for scissors to win.
if choice==1 and computer_choice==2:
    print("Computer wins")
elif choice==2 and computer_choice==1:
    print("You win")
    
#Wining condition for rock to win.
if choice==0 and computer_choice==2:
    print("You win")
elif choice==2 and computer_choice==0:
    print("Computer Wins")
    
#this is the draw condition when both the user and the computer choose same choices like when they both choose rock or paper.
if choice==0 and computer_choice==0:
    print("It is draw")
elif choice==1 and computer_choice==1:
    print("It is draw.")
elif choice==2 and computer_choice==2:
    print("It is draw.")