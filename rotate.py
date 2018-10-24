# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(string, n):
    # Your code here
    i = 0
    new_string = ""
    for s in string:
        if i <= len(string):
            new_number = ord(s) + n
            if new_number == n + 32:
                new_number = 32
            if new_number < 97:
                new_number += 26
            elif new_number > 122:
                new_number -= 26
            new_letter = chr(new_number)
            new_string += new_letter
            i += 1
    return new_string

        


print (rotate ('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))
#>>> ???