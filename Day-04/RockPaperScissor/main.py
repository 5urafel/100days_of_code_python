import random

RPS = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""" ,
       """
            _______
       ---'    ____)____
                  ______)
                 _______)
                _______)
       ---.__________)
       """
       ,
       """
           _______
       ---'   ____)____
                 ______)
              __________)
             (____)
       ---.__(___)
       """
       ]
your_choise = int(input("what do you want to choose? type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(RPS[your_choise])
computer_choise = random.randint(0,2)
print('computer chose: ')
print(RPS[computer_choise])
if your_choise == 0:
    if computer_choise == 0:
        print("It's a draw!")
    elif computer_choise == 1:
        print('You Lose!')
    else:
        print('You Win!')
if your_choise == 1:
    if computer_choise == 0:
        print('You Win!')
    elif computer_choise == 1:
        print("It's a draw!")
    else:
        print('You Lose!')
if your_choise == 2:
    if computer_choise == 0:
        print('You Lose!')
    elif computer_choise == 1:
        print('You Win!')
    else:
        print("It's a draw!")


