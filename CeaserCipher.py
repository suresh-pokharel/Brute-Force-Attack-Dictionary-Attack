
"""Ceaser Cipher Implementation"""


def encrypt(text, k):
    cipher = []
    for character in text:
        # convert character to ascii and add k
        temp = ord(character) - 96   # Assuming message is in lowercases, assign 1 to 26

        # encipher the character
        temp = (temp + k) % 26
        # convert ascii to character
        cipher.append(chr(temp+96))

    return cipher


def decrypt(text, k):
    plaintext = []
    for number in text:
        # decipher the code
        character = (ord(number)-96 - k) % 26

        # convert character to ascii
        temp = chr(character+96)   # Assuming message is in lowercases

        # convert ascii to character
        plaintext.append(temp)

    return plaintext


original_text = "hellopassworld"

# k is number of characters to shift i.e. If k=1, A->B
k = 1
print("Original message: ", original_text)

# encrypt
cipher = encrypt(original_text, k)
print("Encrypted message: ", ''.join(cipher))

# decrypt
plaintext = decrypt(cipher, k)

# join characters to make string
plaintext = "".join(plaintext)
print("Decrypted message: ", plaintext)
