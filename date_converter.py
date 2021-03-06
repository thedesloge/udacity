# Question 5: Date Converter

# Write a procedure date_converter which takes two inputs. The first is 
# a dictionary and the second a string. The string is a valid date in 
# the format month/day/year. The procedure should return
# the date written in the form <day> <name of month> <year>.
# For example , if the
# dictionary is in English,

english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 
6:"June", 7:"July", 8:"August", 9:"September",10:"October", 
11:"November", 12:"December"}

# then  "5/11/2012" should be converted to "11 May 2012". 
# If the dictionary is in Swedish

swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj", 
6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober", 
11:"november", 12:"december"}

# then "5/11/2012" should be converted to "11 maj 2012".

# Hint: int('12') converts the string '12' to the integer 12.

def date_converter(dict, date):
    split_date = date.split("/")
    date = split_date[1]
    year = split_date[2]
    month = int(split_date[0])
    for mon in dict:
        #print("test1")
        #print (month, mon)
        #print(type(month), type(mon))
        if mon == month:
            #print("Test2")
            #print (dic[mon])
            month = dict[mon]
    return date + " " + month + " " + year

def date_converter2(dict, date):
    day, month, year = date.split("/")
    return date + " " + dict[int(month)] + " " + year



print (date_converter2(english, '5/11/2012'))
#>>> 11 May 2012

print (date_converter(english, '5/11/12'))
#>>> 11 May 12

print (date_converter(swedish, '5/11/2012'))
#>>> 11 maj 2012

print (date_converter(english, '1/1/2012'))
#>>> 1 January 2012

print (date_converter(swedish, '12/5/1791'))
#>>> 5 december 1791
