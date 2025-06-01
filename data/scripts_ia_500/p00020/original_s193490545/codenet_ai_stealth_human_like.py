import sys
# bon, on va juste mettre ça en majuscules
alphabets = 'abcdefghijklmnopqrstuvwxyz'
caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in sys.stdin:
    # enlever le dernier caractere, souvent un saut de ligne
    line_without_newline = line[:-1]
    # traduction lettre par lettre
    result = line_without_newline.translate(str.maketrans(alphabets, caps))
    print(result)