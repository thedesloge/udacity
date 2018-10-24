# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    number = ord(letter)
    if number < 97 or number > 122:
        return
    else:
        number += 1
        if number > 122:
            number -= 26
        answer = chr(number)
        return answer


print (shift('a'))
#>>> b
print (shift('n'))
#>>> o
print (shift('z'))
#>>> a