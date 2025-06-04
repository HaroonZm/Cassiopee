# Bon, je refais ce truc, mais j'avoue c'est pas super clair, hein !
still_running = True
while still_running:
    try:
        n = int(input())
        if n == 0:
            break  # Stop le truc si c'est zéro
        mat = []
        # On récupère les lignes du "truc"
        for i in range(n):
            mat.append(list(input()))
        for i in range(n):
            for j in range(len(mat[i])):
                if mat[i][j] == '.':
                    mat[i][j] = ' '  # Franchement, pas fan des espaces, mais bon...
                else:
                    if j > 0:
                        mat[i][j-1] = '+'
                        k = i-1
                        # Je crois que c'est pour mettre des | vers le haut, mais à vérifier...
                        while k >= 0 and mat[k][j-1] == ' ':
                            mat[k][j-1] = '|'
                            k -= 1
                    break  # On s'arrête dès qu'on a trouvé qlq chose
        for r in mat:
            print(''.join(r))
    except Exception as e:
        # Bon, pas sûr que ça serve ici, mais au cas où
        still_running = False