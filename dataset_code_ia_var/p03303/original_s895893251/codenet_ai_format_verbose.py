texte_entree = input()

intervalle_saut = int(input())

texte_reduit = texte_entree[::intervalle_saut]

print(texte_reduit)