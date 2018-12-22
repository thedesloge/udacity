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
    location = 0
    lowercase_text = text.lower()
    if ''.join(reversed(lowercase_text)) == lowercase_text:
        return text
    else:
        for letter in lowercase_text: #looping through the lowercase string
            if letter == lowercase_text[location]: #if the letter we are looking at matches the letter in the index location we are at, make a new string
                print(lowercase_text.index(letter))
                string = lowercase_text[location:lowercase_text.index(letter)] #the new string is from the index location to where we found a matching letter
                if string == string[:: -1]: #check if the string is the same forward and backwards
                    if len(string) > len(longest_found): #if it is, it's a palindrome and we need to save it if it's longer than the longest we have found already
                        longest_found = string #add it to the longest_found list if it's the longest
                    elif len(string) == len(longest_found): #if it's tied for the longest, we add it to the list so we have both
                        longest_found.append(string)
        location += 1

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


#print (longest_subpalindrome_slice('racecar'))
#print (longest_subpalindrome_slice('Racecar'))
print (longest_subpalindrome_slice('RacecarX'))