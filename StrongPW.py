#! python3
# Strong Password Detection
# Write a function that uses regular expressions to make sure the password string
# it is passed is strong. A strong password is defined as one that is at least eight
# characters long, contains both uppercase and lowercase characters, and has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.

import re

password = re.compile(r'''(
    ^(?=.*[a-z])  #at least 1 lowercase characters
    (?=.*[A-Z])   #at least 1 uppercase characters 
    (?=.*[0-9])   #at lease 1 numeric digits
    .{8,}         #at least 8 characters 
    )''', re.VERBOSE)


def checkpass():
    PASS = input('please input a PW:')
    result = password.search(PASS)
    if not result:
        print('your password isn\'t meet the requirements')
        exit()
    else:
        print('ok, your password is passed')


checkpass()
