# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(input):
    if input == []:
        return None
    longest = None # value of longest repeated string of characters
    longest_number = 0 # number of longest string of characters
    potential = 0 #potential new longest char, keeping count for us
    n = 0 #iterator through the list "input"
    current = input[n] #current value of input at n
    next = input[n+1] #next value for comparison
    for entry in input:
        if current == next:
            print (current, next, longest)
            potential += 1
            longest_number += 1
            n += 1
            if current != next:
                if potential > longest_number:
                    longest = current
                #feels like something else goes here, just can't figure out what
                n+= 1
        else:
            #print (current, next, longest)
            current = next
            n += 1
            longest = current
    return longest


#For example,

print (longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

#print (longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

#print (longest_repetition([1,2,3,4,5]))
# 1

#print (longest_repetition([]))
# None

