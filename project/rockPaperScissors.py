import random
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

#Write your code below this line 👇
map = [rock, paper, scissors]
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
pickedComputer = random.randint(0, 2)
# pickedComputer = map[randomComputer]
chooseMe = map[(choose)]

print(f"you picked : {chooseMe}")
print(f"computer picked : {map[pickedComputer]}")

if choose >=3 or choose < 0:
  print("invalid number, you lose. Try again!")
elif choose == 0 and pickedComputer == 2:
  print("You Win!")
elif choose == 2 and pickedComputer == 0:
  print("Computer Wins!")
elif pickedComputer > choose:
  print("Computer Wins!")
elif choose == 1 and pickedComputer == 0:
  print("You Win!")
elif choose == 2 and pickedComputer == 1:
  print("You Win!")
elif choose == pickedComputer:
  print("Draw try again!")