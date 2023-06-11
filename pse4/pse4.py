''' question
Imagine working on software that processes text. A palindrome is a word, phrase, or sequence that reads the same backward as forward.

Create a function named palindrome that determines if a string is a palindrome. This method should take in one string as a parameter. This method should return True if the string is a palindrome.
'''

''' feedback
Nicely done!

Some things to consider:

Maybe we can shorten this a little by combining some of these methods:

def palindrome(s):
    if s == "" or not isinstance(s, str):
        return False

    s = "".join([x.lower() for x in s if x.isalpha()])
    s_rev = s[::-1]

    return s_rev == s
'''

def palindrome(s):
    if not isinstance(s, str):
        return False

    s = "".join([x for x in s if x.isalpha()])
    s = s.lower()
    s_rev = s[::-1]

    return s_rev == s if s != "" else False

print(palindrome("Hello, world!"))
print(palindrome("noon"))
print(palindrome("racecar"))
print(palindrome("mom"))
print(palindrome("kayak"))
print(palindrome("123"))
print(palindrome("poop"))
print(palindrome(""))
print(palindrome(123))
print(palindrome(["hello", "world"]))

''' additional question
What is the time complexity of your solution? Explain.
'''

''' answer
Linear O(n), since the list comprehension (used to find any punctuation/nums/whitespace etc) is essentially a loop, the time complexity increases as the string size grows. 
'''