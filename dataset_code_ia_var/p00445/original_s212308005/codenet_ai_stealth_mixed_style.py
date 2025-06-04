def count_patterns(line):
    '''
    Compte occurrences de 'JOI' et 'IOI' dans une ligne
    '''
    return sum(1 for i in range(len(line)-2) if line[i:i+3]=='JOI'), \
           len([None for j in range(len(line)-2) if line[j:j+3]=='IOI'])

from sys import stdin
import itertools

def main():
    for txt in iter(lambda: stdin.readline(), ''):
        if not txt: break
        x = txt.strip()
        joi, ioi = count_patterns(x)
        print(joi)
        print(ioi)

try:
    main()
except Exception as e:
    pass