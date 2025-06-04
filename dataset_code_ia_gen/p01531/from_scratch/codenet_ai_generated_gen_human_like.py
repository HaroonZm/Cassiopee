s = input()
button_to_consonant = {
    '1': 'k',
    '2': 's',
    '3': 't',
    '4': 'n',
    '5': 'h',
    '6': 'm',
    '7': 'y',
    '8': 'r',
    '9': 'w',
    '0': '',  # special case: only 'ん' on '0U'
}

vowel_map = {
    'T': 'a',
    'L': 'i',
    'U': 'u',
    'R': 'e',
    'D': 'o',
}

# special case for 0U => 'ん' -> nn
# and also 0 with other flicks does not produce except 0U

res = []
for i in range(0, len(s), 2):
    b = s[i]
    d = s[i+1]
    if b == '0' and d == 'U':
        res.append('nn')
    else:
        cons = button_to_consonant[b]
        vowel = vowel_map[d]
        if cons == '':  # this should be only 0U but handled above, so else just ignore
            pass
        elif cons == '' and vowel == 'a':  # 0T does not appear according to problem?
            pass
        else:
            if cons == '':
                res.append(vowel)
            elif vowel == 'a':
                if cons == '':
                    res.append(vowel)
                else:
                    # for a vowel, output just vowel if in 'a' row, but consonant is '' only for 0, handled above
                    res.append(vowel)
            else:
                res.append(cons + vowel)

print(''.join(res))