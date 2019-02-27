
class CeaserCipher(object):
    """Ceaser Cipher Implementation"""
    
    
    def encrypt(self,text, k):
        cipher = []
        for character in text:
            # convert character to ascii and add k
            temp = ord(character) + k

            # convert ascii to character
            cipher.append(chr(temp))

        return cipher


    def decrypt(self,text, k):
        plaintext = []
        for character in text:
            # convert character to ascii and add k
            temp = ord(character) - k

            # convert ascii to character
            plaintext.append(chr(temp))

        return plaintext


obj = CeaserCipher()
plaintext = "Please get $100000 password is: westrvdgaz"

# k is number of characters to shift i.e. If k=1, A->B
k = 5
print("Original message: ", plaintext)

#encrypt
cipher = obj.encrypt(plaintext, k)
print("Encrypted message: ", ''.join(cipher))

# decrypt
plaintext = obj.decrypt(cipher, k)

# join characters to make string
plaintext = "".join(plaintext)
print("Decrypted message: ", plaintext)

