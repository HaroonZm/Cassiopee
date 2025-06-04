z = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_letter(x, i, j):
    pos = z.index(x)
    new_pos = (pos * i + j) % 26
    return z[new_pos]

def find_keys(s):
    for i in range(1, 26, 2):
        for j in range(26):
            word1 = ''.join(encrypt_letter(c, i, j) for c in 'that')
            word2 = ''.join(encrypt_letter(c, i, j) for c in 'this')
            if word1 in s or word2 in s:
                return (i, j)

num_cases = int(input())
for whatever in range(num_cases):
    s = input()
    keys = find_keys(s)
    encrypted_alphabet = ''.join(encrypt_letter(c, keys[0], keys[1]) for c in z)
    # create translation table from encrypted alphabet to normal
    table = str.maketrans(encrypted_alphabet, z)
    print(s.translate(table))