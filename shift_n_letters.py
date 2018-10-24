# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    number = ord(letter)
    if number < 97 or number > 122:
        return
    else:
        number += n
        if number > 122:
            number -= 26
        elif number < 97:
            number += 26
        answer = chr(number)
        return answer


print (shift_n_letters('s', 1))
#>>> t
print (shift_n_letters('s', 2))
#>>> u
print (shift_n_letters('s', 10))
#>>> c
print (shift_n_letters('s', -10))
#>>> i