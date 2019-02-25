"""
      Author  : Suresh Pokharel
      Email   : suresh.wrc@gmail.com
      GitHub  : github.com/suresh021
      URL     : psuresh.com.np
"""

import itertools


class SecurityAttack:
    def __init__(self):
        self.password_length = 5
        self.true_username = "adm"
        self.true_password = "adm"

    def authenticate(self, username, password):
        # compare username and password with their true values
        if (username == self.true_username) and (password == self.true_password):
            print("Success")
            return 1
        else:
            print("Failed")
            return 0

    def iterator(self,length_of_string, alphabets):
        # returns possible combinations of characters of size 'length_of_string' using set 'alphabets'
        yield from itertools.product(*([alphabets] * length_of_string))

    def generate_strings(self, length_of_string, alphabets):
        list_of_string = []
        for x in self.iterator(length_of_string, alphabets):
            temp = ''.join(x)

            # append every new combination to array
            list_of_string.append(temp)
        return list_of_string

    def brute_force(self, string_set):
        for username in string_set:  # loop to find username
            for password in string_set:  # loop to find username
                print('Username: ', username)
                print('Password: ', password)


obj = SecurityAttack()

# assuming string contains small letters and few symbols only
# give all possible characters, numbers and symbols that is possibly included in username or password
alphabets = 'abcdefghijklmnopqrstuvwxyz+@#$%^&'

# what is the length of string? Eg. abc, cab, xys are of length 3
string_length = 1

# get all possible string set ie. (no. of possible characters)^string_length
string_set = obj.generate_strings(string_length, alphabets)

print("Number of possible combinations: ", len(string_set))
print(string_set)
print("Number of possible combinations: ", len(string_set))

obj.brute_force(string_set)

