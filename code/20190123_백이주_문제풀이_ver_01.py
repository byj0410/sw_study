# Q1. 팰린드롬 문자열인지 판별하는 함수를 만드시오.

# def is_palindrome(string):
# [input] string
# [output] boolean
# Hint: arr[::-1]

# False A
def is_palindrome1(string):

    i=0

    while i <= string(len)//2:
        if string[i]==string[string(len)-i]:
            i+=1
        else:
            break

    if i==string(len)//2:
        return True

# A1
def is_palindrome(string):
    string2=string
    string2.reverse()
    return string == string2

# A2
def is_palindrome(string):
    return string == string[::-1]

# A3 [C언어 방법]
def is_palindrome(string):
    length = len(string)

    for index, value in enumerate(string):
        if (string[index]) != string[length-1-i]:
            return False
    return True
