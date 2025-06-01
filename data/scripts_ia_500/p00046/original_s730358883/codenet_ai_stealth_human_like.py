import sys

def main():
    mountains = []  # liste pour garder toutes les hauteurs (j'appelle ça montagnes ici)
    for line in sys.stdin:
        # je suppose que chaque ligne est un nombre float
        mountains.append(float(line.strip()))

    mountains.sort()  # tri, utile pour trouver le max et le min facilement

    difference = mountains[-1] - mountains[0]  # plus haute - plus basse
    print(difference)  # afficher la différence, ça devrait être la réponse

if __name__ == "__main__":
    main()