import getpass
import os


print('----------------------------------------------------------------')
print('                    Cifrado de Vigenere                         ')
print('----------------------------------------------------------------')
print('Es un cifrado basado en diferentes series de caracteres o letras')
print('del cifrado César; estos caracteres forman una tabla que se usa ') 
print('como clave. El cifrado de Vigenere es un cifrado por sustitución')
print('simple polialfabético.')


def leave_sys():
	while True:
		leave = input('¿Desea continuar? (S / N): ').lower()
		if leave == 's':
			main()
		elif leave == 'n':
			os._exit(0)
		else:
			print('Entrada no válida')


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


def main():
    while True:
        try:
            text = input('\nIngrese texto: ').lower()
            if text == '':
                print('El campo está vacío...')
                leave_sys()
            elif text.isnumeric():
                print('El campo es numérico')
                leave_sys()
            elif text.isalnum():
                print('El campo es alfa-numérico')
                leave_sys()
            else:
                # Hide the characters with getpass method
                custom_key = getpass.getpass('Ingrese clave: ').lower()
                encryption = encrypt(text, custom_key)
                print(f'\nEncrypted text: {encryption}\n')
                # decryption = decrypt(encryption, custom_key)
                # print(f'Decrypted text: {decryption}\n')
                leave_sys()
        except:
            print('Entrada no válida...')
            leave_sys()


# If the program is run (instead of imported), run the main:
if __name__ == '__main__':
	main()