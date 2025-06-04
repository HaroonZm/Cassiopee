dic = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}

while True:
    try:
        ligne = raw_input()
        morceaux = ligne.split(',')
        groupe = morceaux[1]
        dic[groupe] = dic[groupe] + 1
    except EOFError:
        print(dic['A'])
        print(dic['B'])
        print(dic['AB'])
        print(dic['O'])
        break