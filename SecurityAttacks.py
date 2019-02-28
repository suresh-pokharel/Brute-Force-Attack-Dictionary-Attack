"""
      Author  : Suresh Pokharel
      Email   : suresh.wrc@gmail.com
      GitHub  : github.com/suresh021
      URL     : psuresh.com.np
"""

import itertools


class SecurityAttack:
    def __init__(self):
        self.true_username = "admin"
        self.true_password = "admin"

    def authenticate(self, username, password):
        # compare username and password with their true values
        if (username == self.true_username) and (password == self.true_password):
            return 1
        else:
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
                print('Testing For username: ', username, 'and password: ', password)

                # supply username and password
                # instead of supplying data to authenticate function, you can call api and check the response
                # your ip may get blocked for sending excessive request

                success = self.authenticate(username, password)

                if success:
                    print("------------------------------------")
                    print("Username: ", username)
                    print("Password: ", password)
                    break

    def dictionary_attack(self):
        # sample of dictionary words are used for testing
        dictionary_words = ['apple', 'orange', 'cat', 'mouse', 'admin', 'user']

        # consider we know the username so, we are supplying password as dictionary words
        username = 'admin'
        for password in dictionary_words:
            print('Testing For username: ', username, 'and password: ', password)
            success = self.authenticate(username, password)
            if success:
                print("------------------------------------")
                print("Username: ", username)
                print("Password: ", password)
                break


# create object of Security Attack
obj = SecurityAttack()

# assuming string contains small letters and few symbols only
# give all possible characters, numbers and symbols that is possibly included in username or password
alphabets = 'abcdefghijklmnopqrstuvwxyz+@#$%^&'

# what is the length of string? Eg. abc, cab, xys are of length 3
string_length = 5

# get all possible string set ie. (no. of possible characters)^string_length
string_set = obj.generate_strings(string_length, alphabets)
print("Number of possible combinations: ", len(string_set))

obj.brute_force(string_set)
# obj.dictionary_attack()

