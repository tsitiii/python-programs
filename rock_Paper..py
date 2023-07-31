#rock paper scissors
rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
images=[rock,paper,scissor]
import random
User_choice=int(input("what do u choice?, type 0 for rock,1 for paper ,2 scissor"))
print(images[User_choice])
comp_choice=random.randint(0,2)
print("Computer choose:")
print(images[comp_choice])
if User_choice>=3 or User_choice<0:
    print("u typed wrong number")
else:   
 if User_choice==0 and comp_choice==2:
    print("yow win")
 elif comp_choice > User_choice:
    print("You lose i win")
 elif comp_choice==User_choice:
    print("no one wins")
 elif comp_choice<User_choice:
    print("You win")

