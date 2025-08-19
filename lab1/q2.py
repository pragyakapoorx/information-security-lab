"""
Encrypt the message "the house is being sold tonight" using one of the following ciphers.
Ignore the space between words. Decrypt the message to get the original plaintext:
"""
#key = dollars
def vignere_encrypt(plaintext, key):
    ciphertext = ""
    n = len(key)
    j = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext += chr((ord(plaintext[i]) - 65 + ord(key[j % n]) - 97) % 26 + 65)
            j = j + 1

        else:
            ciphertext += plaintext[i]
    return ciphertext

def vignere_decrypt(ciphertext, key):
    plaintext = ""
    n = len(key)
    j=0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            plaintext += chr((ord(ciphertext[i])-65-ord(key[j%n])+97)%26+97)
            j=j+1
        else:
            plaintext += ciphertext[i]
    return plaintext

#key = 7
def autokey_encrypt(plaintext, key):
    ciphertext = ""
    key_stream = [key] + [ord(c) - 65 for c in plaintext]  # Convert plaintext to key stream
    for i in range(len(plaintext)):
        shift = key_stream[i]
        encrypted_char = chr((ord(plaintext[i]) - 65 + shift) % 26 + 65)
        ciphertext += encrypted_char
    return ciphertext

def autokey_decrypt(ciphertext, key):
    plaintext = ""
    key_stream = [key]
    for i in range(len(ciphertext)):
        shift = key_stream[i]
        decrypted_char = chr((ord(ciphertext[i]) - 65 - shift + 26) % 26 + 65)
        plaintext += decrypted_char
        key_stream.append(ord(decrypted_char) - 65)  # Append decrypted char to key stream
    return plaintext

if __name__ == "__main__":
    plaintext = input("Please enter plaintext: ")
    plaintext = plaintext.replace(" ", "").upper()

    key1 = input("Enter key for Vignere cipher: ")
    vignere_ciphertext = vignere_encrypt(plaintext, key1)
    print("Encrypted: ", vignere_ciphertext)
    print("Decrypted: ", vignere_decrypt(vignere_ciphertext, key1))

    key2 = int(input("Enter key for Autokey cipher: "))
    autokey_ciphertext = autokey_encrypt(plaintext, key2)
    print("Encrypted: ", autokey_ciphertext)
    print("Decrypted: ", autokey_decrypt(autokey_ciphertext, key2))