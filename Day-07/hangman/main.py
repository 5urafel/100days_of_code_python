import random
import os

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
''')
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# random word ggenerator

words = ["hangman", "computer", "python", "program", "gaming", "coding", "challenge"]
selected_word = random.choice(words).lower()
print(selected_word)

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


reveal_word = "_ "*len(selected_word)
def substitute(guessed_letter):
    global reveal_word
    for i in range (len(selected_word)):
        if selected_word[i] == guessed_letter:
            reveal_word = reveal_word[:i*2] + guessed_letter + reveal_word[i*2+1:]
    return reveal_word





life = len(HANGMANPICS)
count = 0
guessed_letter = input("gusse a letter:")
while life > 0 :
    substituted_word = substitute(guessed_letter)
    print(substituted_word)
    if guessed_letter in selected_word:
        print(f"you guessed {guessed_letter}. it is in the word")
        if count > 0:
            print(HANGMANPICS[count])
        if "_ " not in substituted_word:
            print("You won the game")
            break
    else:
        count += 1
        if count >= 6:
            print("Game over! You lost the game ")
            break
        print(f"you guessed letter {guessed_letter},that is not in the word .you lose a life.")
        print(HANGMANPICS[count])
        life -= 1

    clean()
    guessed_letter = input("gusse a letter:")







