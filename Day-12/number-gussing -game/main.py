import random

computer_number = random.randint(1,100)
print(computer_number)


def hard():
    for i in range(5,0,-1):
        print(f"you have {i} attempts remaining to guesse the number")
        guessed_number = int(input("Make a Guess: "))
        if computer_number == guessed_number:
            print(f"you got it. you guessed {guessed_number}")
            break
        elif computer_number < guessed_number:
            print("Too high")
            if i == 1:
                print("you've run out of guesses, you lose!")
            else:
                print("Guess again")
        else:
            print("Too low")
            if i == 1:
                print("you've run out of guesses, you lose!")
            else:
                print("Guess again")
def easy():
    for i in range(10,0,-1):
        print(f"you have {i} attempts remaining to guesse the number")
        guessed_number = int(input("Make a Guess: "))
        if computer_number == guessed_number:
            print(f"you got it. you guessed {guessed_number}")
            break
        elif computer_number < guessed_number:
            print("Too high")
            if i == 1:
                print("you've run out of guesses, you lose!")
            else:
                print("Guess again")
        else:
            print("Too low")
            if i == 1:
                print("you've run out of guesses, you lose!")
            else:
                print("Guess again")

print("Wellcome to a number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty  = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty.lower() == "easy":
     easy()
elif difficulty.lower() == "hard":
    hard()
else:
    print("wrong input")