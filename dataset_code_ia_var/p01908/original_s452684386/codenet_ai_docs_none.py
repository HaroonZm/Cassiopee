def make_alphabet(now_alphabet, alphabet):
    next_alphabet = []
    for n_al in now_alphabet:
        for al in alphabet:
            next_alphabet.append(n_al+al)
    return next_alphabet

a = int(input())
b = []
for _ in range(a):
    b.append(input())
alphabet = [chr(ch) for ch in range(97,123)]
now_alphabet = alphabet
count = 0
flag = 0

while flag == 0:
    letter = []
    for word in b:
        for i in range(len(word)-count):
            letter.append(word[i:i+1+count])
    rem = list(set(now_alphabet) - set(letter))
    if rem != []:
        print(sorted(rem)[0])
        flag = 1
    count += 1
    now_alphabet = make_alphabet(now_alphabet, alphabet)