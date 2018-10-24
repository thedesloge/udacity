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
            new_number = ord(s) + n #finding the ascii value of each char and adding the shift
            if new_number == n + 32: #checking to see if initial character was a space
                new_number = 32 #keeping space as a space: I want to add this to the string at this point and keep iterating through the list
            while new_number < 97: #if the number is not between a and z, getting it back into that range
                new_number += 26
            while new_number > 122: #if the number is not between a and z, getting it back into that range
                new_number -= 26
            new_letter = chr(new_number) #changing ascii number back into letter
            new_string += new_letter #adding letter onto string
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