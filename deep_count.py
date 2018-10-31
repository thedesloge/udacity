def deep_count(p):
    count = 0
    for e in p:
        count += 1
        if is_list(e):
            count += deep_count(p)
    return count






print (deep_count([1, 2, 3]))
#>>> 3

# The empty list still counts as an element of the outer list
print (deep_count([1, [], 3])) 
#>>> 3 

print (deep_count([1, [1, 2, [3, 4]]]))
#>>> 7

print (deep_count([[[[[[[[1, 2, 3]]]]]]]]))
#>>> 10

 