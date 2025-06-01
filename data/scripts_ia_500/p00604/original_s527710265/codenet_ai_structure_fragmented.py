def lire_entier():
	try:
		return int(input())
	except:
		exit()

def lire_liste_entiers():
	return list(map(int, input().split()))

def trier_liste(liste):
	liste.sort()

def accumuler_prefixes(liste):
	for i in range(len(liste) - 1):
		incrementer_element_suivant(liste, i)

def incrementer_element_suivant(liste, index):
	liste[index + 1] += liste[index]

def calculer_somme(liste):
	return sum(liste)

def main():
	while True:
		n = lire_entier()
		a = lire_liste_entiers()
		trier_liste(a)
		accumuler_prefixes(a)
		resultat = calculer_somme(a)
		afficher_resultat(resultat)

def afficher_resultat(resultat):
	print(resultat)

main()