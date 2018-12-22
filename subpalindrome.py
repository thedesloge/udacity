# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    longest_found = []
    location = -1
    lowercase_text = text.lower()
    if ''.join(reversed(lowercase_text)) == lowercase_text:
        return lowercase_text
    else:
        for letter in lowercase_text: #looping through the lowercase string
            location += 1
            curr_index = location
            # Now loop over every character to the right, looking for a palindrome
            for letter2 in lowercase_text[location:]:
                #current index to remember which character we are away from the starting letter
                curr_index += 1
                # If we have found a letter equal to the one we are searching enter 
                if letter == letter2:
                    #Get the string from our letter to the current index
                    string = lowercase_text[location:curr_index]
                    # Check if its a palindrome
                    if len(string) == 1 and len(lowercase_text) != 1:
                        continue
                    if string == string[:: -1]: #check if the string is the same forward and backwards
                        if len(string) > len(longest_found): #if it is, it's a palindrome and we need to save it if it's longer than the longest we have found already
                            longest_found = string #add it to the longest_found list if it's the longest
                        elif len(string) == len(longest_found): #if it's tied for the longest, we add it to the list so we have both
                            longest_found = longest_found + " " + string


        return longest_found






def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print (longest_subpalindrome_slice('racecar')) #racecar
print (longest_subpalindrome_slice('Racecar')) #racecar
print (longest_subpalindrome_slice('RacecarX')) #racecar
print (longest_subpalindrome_slice('Race carr')) #rr
print (longest_subpalindrome_slice('')) #(space)
print (longest_subpalindrome_slice('something rac e car going')) #g rac e car g
print (longest_subpalindrome_slice('xxxxx')) #xxxxx
print (longest_subpalindrome_slice('Mad am I ma dam.')) #mad am I am dam
print (longest_subpalindrome_slice('a')) #a

