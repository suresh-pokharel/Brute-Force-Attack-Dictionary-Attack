
"""
Consider a paragraph of cipher text enciphered with simple substitution cipher. Use statistical method to decipher
the paragraph.You can use any programming language of your choice.

"""


# frequency of letters used analysis by oxford dictionaries
# https://en.oxforddictionaries.com/explore/which-letters-are-used-most/
"""
E	11.1607%	56.88	M	3.0129%	15.36
A	8.4966%	43.31	H	3.0034%	15.31
R	7.5809%	38.64	G	2.4705%	12.59
I	7.5448%	38.45	B	2.0720%	10.56
O	7.1635%	36.51	F	1.8121%	9.24
T	6.9509%	35.43	Y	1.7779%	9.06
N	6.6544%	33.92	W	1.2899%	6.57
S	5.7351%	29.23	K	1.1016%	5.61
L	5.4893%	27.98	V	1.0074%	5.13
C	4.5388%	23.13	X	0.2902%	1.48
U	3.6308%	18.51	Z	0.2722%	1.39
D	3.3844%	17.25	J	0.1965%	1.00
P	3.1671%	16.14	Q	0.1962%	(1)
"""
# array of character is sorted by frequency provided by oxforddictionaries.com in high frequent to low order
letters_sorted_by_frequency_known = ['E', 'A', 'R', 'I', 'O', 'T', 'N', 'S', 'L', 'C', 'U', 'D', 'M', 'P', 'H', 'G', 'B', 'F', 'Y', 'W', 'K', 'V', 'X', 'Z', 'J', 'Q']
key = ''.join(letters_sorted_by_frequency_known)
print(key)

def count_frequency(text):
    # initialize frequency count by 0
    frequency_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # convert all text to uppercase
    text = text.upper()

    for letter in text:
        # find ascii of character
        ascii_val = ord(letter)

        # find character's index and increase the counter
        if 65 <= ascii_val <= 90:

            # subtract 65 to make value ranges from 0 to 25 i.e. 0=>A, 1=> B and so on
            index = ascii_val - 65

            # increase counter
            frequency_count[index] += 1

    return frequency_count


def sort_character_with_frequency(frequency_count):
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']

    # sort frequency in descending order, swap characters at same time

    for i in range(25):
        for j in range(i+1, 26):
            if frequency_count[i] < frequency_count[j]:
                # swap frequency
                temp = frequency_count[j]
                frequency_count[j] = frequency_count[i];
                frequency_count[i] = temp

                # swap character
                temp = characters[j]
                characters[j] = characters[i];
                characters[i] = temp

    return characters


def map_substitution(text, char_set_source, char_set_destination):
    # text is enciphered text to decipher
    # char_set_source should be replaced with char_set_destination
    deciphered_text = []
    # convert all text to uppercase
    text = text.upper()

    for letter in text:
        # if letter is a character
        if 65 <= ord(letter) <= 90:
            # find index of letter in source_char_set
            index = char_set_source.index(letter)

            # replace in the character with same index destination character
            deciphered_text.append(char_set_destination[index])
        else:
            # append as it is
            deciphered_text.append(letter)

    return deciphered_text


enciphered_message = "ex el ayls xg laa kgf ayjk jkydyjxad ec xka quyecxaox el daquyjai fexk xka jgddalqgciech uaxxad ec xka jeqkad yuqkyrax. iajdsqxegc el vzlx yl ayls, rs hgech mdgt xka jeqkad yuqkyrax ryjn xg xka quyec yuqkyrax. fkac hacadyxech nasl ex el qgqzuyd xg zla y nas fgdi, a.h. 'pardy' xg hacadyxa ex, lecja ex el tzjk aylead xg datatrad y nas fgdi jgtqydai xg y dycigt vztrua gm 26 jkydyjxadl. zlech xka nasfgdi 'pardy', xka nas fgzui rajgta:"
frequency_array = count_frequency(enciphered_message)
print(frequency_array)

chars = sort_character_with_frequency(frequency_array)
print(chars)

deciphered_text = map_substitution(enciphered_message, chars, letters_sorted_by_frequency_known)

# glue characters
deciphered_text = ''.join(deciphered_text)
print(deciphered_text)