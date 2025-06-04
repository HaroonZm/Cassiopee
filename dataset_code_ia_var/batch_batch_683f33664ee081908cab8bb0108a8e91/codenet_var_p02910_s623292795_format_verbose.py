import re

input_string = input()

pattern_no_consecutive_L_or_R = re.compile(r'^([^L][^R])*[^L]?$')

if pattern_no_consecutive_L_or_R.match(input_string):
    print('Yes')
else:
    print('No')