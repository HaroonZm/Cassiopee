def count_characters(word, dic, kcs, kcs2, kcs2_1):
    prev1 = None
    i = 0
    l = len(word)
    while i < l:
        c = word[i]
        # Vérifie si on peut former une paire spéciale (ex : 'ld', 'mp'...)  
        if c in kcs2_1 and i < l - 1:
            c2 = word[i + 1]
            pair = c + c2
            if pair in kcs2:
                if prev1 != None:
                    dic[prev1][pair] += 1
                prev1 = pair
                i += 2
                continue
        # Sinon, on compte le caractère actuel  
        if prev1 != None:
            dic[prev1][c] += 1
        prev1 = c
        i += 1

kcs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
kcs2 = ["ld", "mb", "mp", "nc", "nd", "ng", "nt", "nw", "ps", "qu", "cw", "ts"]
kcs2_1 = ["l", "m", "n", "p", "q", "c", "t"]

n = int(input())
dic = {}

# Crée les tables d'occurence pour chaque lettre et paire spéciale
for key in kcs + kcs2:
    table = {}
    for key2 in kcs + kcs2:
        table[key2] = 0
    dic[key] = table

# Pour chaque mot entré, compte les transitions caractère/paire
for i in range(n):
    words = input().split()
    for word in words:
        count_characters(word, dic, kcs, kcs2, kcs2_1)

# Trouve la transition la plus fréquente depuis chaque entrée
for key in kcs + kcs2:
    occurence_table = dic[key]
    max_c = ""
    max_n = 0
    for k, v in occurence_table.items():
        if v > max_n:
            max_n = v
            max_c = k
    print(key, max_c, max_n)