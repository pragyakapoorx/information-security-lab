"""
Encrypt the message "Confidential Data" using DES with the following key: "A1B2C3D4".
Then decrypt the ciphertext to verify the original message.
"""
from Crypto.Cipher import DES

def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)

key = b'A1B2C3D4'
text1 = b'Confidential Data'

des = DES.new(key, DES.MODE_ECB)

padded_text = pad(text1)
encrypted_text = des.encrypt(padded_text)

print(encrypted_text)
print(des.decrypt(encrypted_text))