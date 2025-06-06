import random

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

index = random.randint(0, len(words) - 1)
selected_word = words[index]
print(selected_word)


blank = ''
for letter in selected_word:
        blank += "_ "

updated_guessed_word = ""

# for i in range(len(selected_word)):
#     guessed_letter = input('Guess a letter: ')
#     if selected_word[i] == guessed_letter:
#         updated_guessed_word += guessed_letter  # If the letter matches, reveal it
#     else:
#         updated_guessed_word += blank[i]  # Otherwise, keep the current character
# print( updated_guessed_word)




# life_count = 0
# while life_count < 7:
#     guessed_letter = input('Guess a letter: ')

    # else:
    #     life_count += 1
    #     print(f'you guessed {guessed_letter} ,that is not in the word, you lost a life')
    #     print(HANGMANPICS[life_count ])



