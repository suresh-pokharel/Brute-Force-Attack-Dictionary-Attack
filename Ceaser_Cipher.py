
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
