def process_queries(n):
    """
    Traite une séquence de requêtes de manipulation de bits sur un registre de 64 bits.

    Args:
        n (int): Nombre de requêtes à traiter. 

    Les requêtes sont lues en entrée standard et sont de la forme :
        0 x : Affiche 0 si le bit x vaut 0, sinon affiche 1.
        1 x : Met le bit x à 1.
        2 x : Met le bit x à 0.
        3 x : Inverse la valeur du bit x.
        4   : Affiche 1 si tous les bits valent 1, sinon affiche 0.
        5   : Affiche 1 si au moins un bit vaut 1, sinon affiche 0.
        6   : Affiche 1 si tous les bits valent 0, sinon affiche 0.
        7   : Affiche le nombre de bits à 1.
        8   : Affiche la valeur entière représentée par le registre.
    """
    # Initialisation du registre de 64 bits sous forme de liste de chaînes '0'
    num = ["0" for _ in range(64)]

    for _ in range(n):
        # Lecture et découpage de la requête
        query = input().split()
        # Sélection de l'opération en fonction du premier argument
        if query[0] == "0":
            # Affiche 0 si le bit x vaut 0, sinon affiche 1
            bit_index = int(query[1])
            print(0 if num[bit_index] == "0" else 1)
        elif query[0] == "1":
            # Met le bit x à 1
            bit_index = int(query[1])
            num[bit_index] = "1"
        elif query[0] == "2":
            # Met le bit x à 0
            bit_index = int(query[1])
            num[bit_index] = "0"
        elif query[0] == "3":
            # Inverse le bit x (toggle)
            bit_index = int(query[1])
            num[bit_index] = "1" if num[bit_index] == "0" else "0"
        elif query[0] == "4":
            # Vérifie si tous les bits sont à 1
            print("1" if num.count("1") == 64 else "0")
        elif query[0] == "5":
            # Vérifie si au moins un bit vaut 1
            print("1" if num.count("1") >= 1 else "0")
        elif query[0] == "6":
            # Vérifie si tous les bits sont à 0
            print("1" if num.count("1") == 0 else "0")
        elif query[0] == "7":
            # Affiche le nombre de bits à 1
            print(num.count("1"))
        elif query[0] == "8":
            # Affiche la valeur décimale du registre traité comme un nombre binaire (bit 0 = LSB)
            print(int("".join(num[::-1]), 2))

def main():
    """
    Fonction principale du programme, charge la lecture du nombre de requêtes et appelle le traitement.
    """
    n = int(input())
    process_queries(n)

if __name__ == "__main__":
    main()