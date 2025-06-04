c = input()
def check_vowel(x):
    return x in ['a', 'i', 'u', 'e', 'o']
if check_vowel(c):
    import sys
    sys.stdout.write('vowel\n')
else:
    for s in ['consonant']:
        print(s)