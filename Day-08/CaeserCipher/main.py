# logo
print('''
  ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_|   
''')

def encryption(plain_message,shift_number):
    encrypted_text = ''
    for char in plain_message:
        if char.isalpha():
            if char.islower():
                encrypted_char =  chr(((ord(char) - ord('a') + shift_number) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_number) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decryption(encrypted_message ,shift_number):
    plain_message = ''
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_number) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_number) % 26) + ord('A'))
            plain_message += decrypted_char
        else:
            plain_message += char
    return plain_message

execution = 'yes'
while execution.lower() == 'yes':
    action = input("Type 'encode' to encrypt ,Type 'decode' to decrypt : \n")

    if action.lower() == 'encode':
        plain_message = input("Type your Message: \n")
        shift_number = int(input("Type the Shift Number: \n"))
        encrypted_text = encryption(plain_message, shift_number)
        print(f'Here is the encoded result: {encrypted_text}')
    elif action.lower() == 'decode':
        encrypted_message = input("Type your Encrypted Message: \n")
        shift_number = int(input("Type the Shift Number: \n"))
        plain_message = decryption(encrypted_message, shift_number)
        print(f'Here is the decoded result: {plain_message}')
    execution = input("Type 'yes' if you want to go again, otherwise type 'no'")










