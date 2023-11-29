import base64

def custom_encrypt(text):
    reversed_text = text[::-1]
    factor = len(text) * (2.71828 ** 2)
    encrypted_text = ''.join(chr(ord(char) * int(factor)) for char in reversed_text)
    encoded_text = base64.b64encode(encrypted_text.encode('utf-8')).decode()
    return encoded_text

def custom_decrypt(encoded_text):
    encrypted_text = base64.b64decode(encoded_text.encode('utf-8')).decode()
    factor = len(encrypted_text) * (2.71828 ** 2)
    decrypted_text = ''.join(chr(ord(char) // int(factor)) for char in encrypted_text[::-1])
    return decrypted_text


command = input("Enter command (enc/dec): ").lower()

if command == "enc":
    word_to_encrypt = input("Enter word to encrypt: ")
    encrypted_word = custom_encrypt(word_to_encrypt)
    print("Encrypted:", encrypted_word)

elif command == "dec":
    encoded_text_to_decrypt = input("Enter encoded text to decrypt: ")
    decrypted_word = custom_decrypt(encoded_text_to_decrypt)
    print("Decrypted:", decrypted_word)

else:
    print("Invalid command. Please enter 'enc' or 'dec'.")
