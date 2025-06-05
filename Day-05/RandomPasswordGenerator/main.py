import random
letters = ['a' ,'b' ,'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i' ,'j' ,'k' ,'l'
    ,'m' ,'n' ,'o' ,'p' ,'q' ,'r' ,'s' ,'t' ,'u' ,'v' ,'w' ,'x' ,'y' , 'z' ,
           'A' ,'B' ,'C' ,'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,
           'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z' ]

numbers = ['0' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']
symbols = ['~' ,'!' ,'@' ,'#' ,'$' ,'%' ,'^' ,'&' ,'*' ,'(' ,')' ,'_' ,'=' ,'-' ,'+' ]

n_letters = int(input('how many letters would you like in your password? \n'))
n_numbers = int(input('how many numbers? \n'))
n_symbols = int(input('how many symbols? \n'))


chosen_characters = []
for i in range(n_letters):
    random_letter_index = random.randint(0, len(letters) - 1)
    chosen_characters.append(letters[random_letter_index])
print(chosen_characters)


for i in range(n_numbers):
    random_number_index = random.randint(0, len(numbers) - 1)
    chosen_characters.append(numbers[random_number_index])
print(chosen_characters)


for i in range(n_symbols):
    random_symbol_index = random.randint(0, len(symbols) - 1)
    chosen_characters.append(symbols[random_symbol_index])
print(chosen_characters)


random.shuffle(chosen_characters)
print(chosen_characters)

password = ''
for i in chosen_characters:
    password += i
print(password)


