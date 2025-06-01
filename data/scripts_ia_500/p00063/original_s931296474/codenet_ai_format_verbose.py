# encoding=utf-8


import sys


palindrome_count = 0


for input_line in sys.stdin:
    
    current_word = input_line.rstrip('\n')
    
    reversed_word = current_word[::-1]
    
    if current_word == reversed_word:
        
        palindrome_count += 1


print(palindrome_count)