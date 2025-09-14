"""
lab1:
Scenario
You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

it should accept exactly one argument - a string;
it should return a list of words created from the string, divided in the places where the string contains whitespaces;
if the string is empty, the function should return an empty list;
its name should be mysplit()
"""


def my_split(_str):
    return _str.split()


"""
lab2:
Scenario
You are already familiar with the Caesar cipher, and this is why we want you to improve the code we showed you recently.

The original Caesar cipher shifts each character by one: a becomes b, z becomes a, and so on. Let's make it a bit harder, and allow the shifted value to come from the range 1..25 inclusive.

Moreover, let the code preserve the letters' case (lower-case letters will remain lower-case) and all non-alphabetical characters should remain untouched.

Your task is to write a program which:

asks the user for one line of text to encrypt;
asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
prints out the encoded text.
Test your code using the data we've provided.

Test data
Sample input:

abcxyzABCxyz 123
2

Sample output:

cdezabCDEzab 123

Sample input:

The die is cast
25

Sample output:

Sgd chd hr bzrs
"""


def get_next_alpha(letter, step):
    a, A = ord("a"), ord("A")
    if letter.isalpha():
        return chr((ord(letter) + step - a) % 26 + a) if letter.islower() else chr((ord(letter) + step - A) % 26 + A)
    return letter


def cipher(_str, step):
    return "".join(get_next_alpha(letter, step) for letter in _str)


"""
lab3:
Scenario
Do you know what a palindrome is?

It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

Your task is to write a program which:

asks the user for some text;
checks whether the entered text is a palindrome, and prints result.
Note:

assume that an empty string isn't a palindrome;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent;
there are more than a few correct solutions - try to find more than one.
Test your code using the data we've provided.

Test data
Sample input:

Ten animals I slam in a net

Sample output:

It's a palindrome


Sample input:

Eleven animals I slam in a net

Sample output:

It's not a palindrome
"""


def is_palindrome(_str):
    _str = _str.lower().replace(" ", "")
    return _str == _str[::-1]


"""
lab4:
Scenario
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
Test your code using the data we've provided.

Test data
Sample input:

Listen
Silent

Sample output:

Anagrams


Sample input:

modern
norman

Sample output:

Not anagrams
"""


def is_anagram(_str1, _str2):
    if _str1 == _str2 == " ":
        return False
    else:
        _str1, _str2 = "".join(sorted(list(_str1.lower().replace(" ", "")))), "".join(
            sorted(list(_str2.lower().replace(" ", ""))))
        return _str1 == _str2


"""
lab5:
Scenario
Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

1 January 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 is the digit we searched for and found.

Your task is to write a program which:

asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY - actually, the order of the digits doesn't matter)
outputs the Digit of Life for the date.
Test your code using the data we've provided.

Test data
Sample input:

19991229

Sample output:

6


Sample input:

20000101

Sample output:

4
"""


def sum_it_till_last_digit(number):
    _str = str(number)
    while len(_str) > 1:
        _str = str(sum(list(map(int, list(_str)))))
    return int(_str)


"""
lab5:
Scenario
Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?

For example:

if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
Hints:

you should use the two-argument variants of the pos() functions inside your code;
don't worry about case sensitivity.
Test your code using the data we've provided.

Test data
Sample input:

donor
Nabucodonosor

Sample output:

Yes


Sample input:

donut
Nabucodonosor

Sample output:

No
"""


# this is not effiecinet but solves the problem
def finding(_str1, _str2):
    word = ""
    for index, item in enumerate(_str2):
        for letter in _str1:
            if item == letter and _str1.find(letter) >= index:
                word += letter
                break
    return word == _str2


def main():
    for test_data in (("abcxyzABCxyz 123", 2), ("The die is cast", 25)):
        print(cipher(*test_data), end=", ")
    print()

    for test_data in ("Ten animals I slam in a net", "Eleven animals I slam in a net"):
        if is_palindrome(test_data):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

    for test_data in (("Listen", "Silent"), ("modern", "norman")):
        if is_anagram(*test_data):
            print("Yes, it's a anagram")
        else:
            print("No, it's not anagram")

    for number in 19991229, 20000101:
        print(sum_it_till_last_digit(number), end=", ")

    for test_data in (("Nabucodonosor", "donor"), ("Nabucodonosor", "donut")):
        print(finding(*test_data))


if __name__ == "__main__":
    main()
