# Define a procedure rabbits that takes as input a number n, and returns a
# number that is the value of the nth number in the rabbit sequence.
# For example, rabbits(10) -> 35. (It is okay if your procedure takes too
#                                long to run on inputs above 30.)


def rabbits(n):
    if n < 1:
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)





        


print (rabbits(10))
#>>> 35