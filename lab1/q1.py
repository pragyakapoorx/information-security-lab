"""
Encrypt the message "I am learning information security" using one of the following ciphers.
Ignore the space between words. Decrypt the message to get the original plaintext:
"""
def mod_inverse(a, m):
    # Compute modular inverse of a mod m using Extended Euclidean Algorithm
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join(chr(n + ord('A')) for n in numbers)


def additive_encrypt(plaintext_nums, key):
    return [(x + key) % 26 for x in plaintext_nums]


def additive_decrypt(ciphertext_nums, key):
    return [(y - key) % 26 for y in ciphertext_nums]


def multiplicative_encrypt(plaintext_nums, key):
    return [(key * x) % 26 for x in plaintext_nums]


def multiplicative_decrypt(ciphertext_nums, key):
    inv_key = mod_inverse(key, 26)
    if inv_key is None:
        raise ValueError("Multiplicative key has no modular inverse!")
    return [(inv_key * y) % 26 for y in ciphertext_nums]


def affine_encrypt(plaintext_nums, a, b):
    return [(a * x + b) % 26 for x in plaintext_nums]


def affine_decrypt(ciphertext_nums, a, b):
    inv_a = mod_inverse(a, 26)
    if inv_a is None:
        raise ValueError("Multiplicative key a has no modular inverse!")
    return [(inv_a * (y - b)) % 26 for y in ciphertext_nums]


def main():
    plaintext = "I am learning information security"
    # Remove spaces and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()

    # Convert plaintext to numbers
    plaintext_nums = text_to_numbers(plaintext)

    print("Original Plaintext:", plaintext)

    # Additive cipher
    additive_key = 20
    encrypted_add = additive_encrypt(plaintext_nums, additive_key)
    decrypted_add = additive_decrypt(encrypted_add, additive_key)
    print("\nAdditive Cipher:")
    print("Encrypted:", numbers_to_text(encrypted_add))
    print("Decrypted:", numbers_to_text(decrypted_add))

    # Multiplicative cipher
    multiplicative_key = 15
    encrypted_mul = multiplicative_encrypt(plaintext_nums, multiplicative_key)
    decrypted_mul = multiplicative_decrypt(encrypted_mul, multiplicative_key)
    print("\nMultiplicative Cipher:")
    print("Encrypted:", numbers_to_text(encrypted_mul))
    print("Decrypted:", numbers_to_text(decrypted_mul))

    # Affine cipher
    affine_a, affine_b = 15, 20
    encrypted_aff = affine_encrypt(plaintext_nums, affine_a, affine_b)
    decrypted_aff = affine_decrypt(encrypted_aff, affine_a, affine_b)
    print("\nAffine Cipher:")
    print("Encrypted:", numbers_to_text(encrypted_aff))
    print("Decrypted:", numbers_to_text(decrypted_aff))


if __name__ == "__main__":
    main()