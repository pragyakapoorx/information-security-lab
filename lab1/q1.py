"""
Encrypt the message "I am learning information security" using one of the following ciphers.
Ignore the space between words. Decrypt the message to get the original plaintext:
"""

#Additive cipher with key = 20
def encrypt_additive(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if 'a' <= char <= 'z':
            val = ord(char) - ord('a')
            encrypted_val = (val+key)%26
            ciphertext += chr(encrypted_val + ord('a'))
        elif 'A' <= char <= 'Z':
            val = ord(char) - ord('A')
            encrypted_val = (val+key)%26
            ciphertext += chr(encrypted_val + ord('A'))
        else:
            ciphertext += char

    return ciphertext

#Multiplicative cipher with key = 15
def encrypt_multiplicative(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if 'a' <= char <= 'z':
            val = ord(char) - ord('a')
            encrypted_val = (val * key) % 26
            ciphertext += chr(encrypted_val + ord('a'))
        elif 'A' <= char <= 'Z':
            val = ord(char) - ord('A')
            encrypted_val = (val * key) % 26
            ciphertext += chr(encrypted_val + ord('A'))
        else:
            ciphertext += char

    return ciphertext

#Affine cipher with key = (15, 20)
def encrypt_affine(plaintext, key1, key2):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((key1 * ( ord(char) - ord('A') ) + key2) %26 + ord('A'))
            else:
                ciphertext += chr((key1 * (ord(char) - ord('a')) + key2) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext

if __name__ == "__main__":

    while True:
        print("\n1. Additive Cipher")
        print("2. Multiplicative Cipher")
        print("3. Affine Cipher")

        choice = input("Enter choice: ")

        if choice == '1':
            plaintext = input("Please enter plaintext: ")
            key = int(input("Enter key "))
            ciphertext = encrypt_additive(plaintext, key)
            print(f"Encrypted text: {ciphertext}")
        elif choice == '2':
            plaintext = input("Please enter plaintext: ")
            key = int(input("Enter key: "))
            ciphertext = encrypt_multiplicative(plaintext, key)
            print(f"Encrypted text: {ciphertext}")

        elif choice == '3':
            plaintext = input("Please enter plaintext: ")
            key1 = int(input("Enter key: "))
            key2 = int(input("Enter next key: "))
            ciphertext = encrypt_affine(plaintext, key1, key2)
            print(f"Encrypted text: {ciphertext}")



   # print(f"Encrypted text: {ciphertext}")     #TODO why is plaintext getting changed

"""
def encrypt_word_additive(plaintext, key):
    ciphertext = plaintext      #List
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(plaintext)):
        letter_index = alphabet.index(plaintext[i].lower())
        ciphertext[i] = alphabet[(letter_index + key)%26]

    ciphertext = "".join(ciphertext)
    return ciphertext
"""