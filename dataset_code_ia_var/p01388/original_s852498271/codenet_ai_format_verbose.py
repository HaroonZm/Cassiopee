lettres_entrees = list(input())

nombre_k = lettres_entrees.count('K')
nombre_u = lettres_entrees.count('U')
nombre_c = lettres_entrees.count('C')
nombre_p = lettres_entrees.count('P')

nombre_maximal_de_mots_KUCP = min(nombre_k, nombre_u, nombre_c, nombre_p)

print(nombre_maximal_de_mots_KUCP)