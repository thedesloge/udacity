# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)'
# Non-uppercase words should remain unchaged.
import re

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    # Your code here.
    index = -1
    answer = ''
    split_string = list(word)
    for letter in split_string:
        finding_letters = re.findall('[A-Z]', word)
        if len(word) != len(finding_letters):
            return str(word)
        multiple = str(10**(abs(index) - 1))
        answer = answer + "+" + (split_string[index]) + '*' + multiple
        index = index - 1
    if re.search('[+]', answer):
        answer = answer[1:]
    return str(answer)

print (compile_word('YOU'))
print (compile_word('+'))