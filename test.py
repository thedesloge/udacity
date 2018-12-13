# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.
"""Challenge: Given the program template below, implement four functions that manipulate a global variable
count as follows. The function reset() sets the value of
count to be zero, the function increment() adds one to
count, the function decrement() subtracts one from
count, and the function print_count() that prints
the value of count to the console"""

def reset():
    global count
    count = 0
def increment():
    global count
    count += 1
def decrement():
    global count
    count -= 1
def print_count():
    print (count)


###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
# 1
# 2
# -2