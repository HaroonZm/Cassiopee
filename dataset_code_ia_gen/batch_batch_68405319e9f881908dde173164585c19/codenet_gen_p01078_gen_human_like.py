import math

def main():
    N, K = map(int, input().split())
    # Le nombre de sommets du polygone est N
    # Chaque sommet est relié au (K-1)-ième point suivant
    # L'angle entre deux sommets consécutifs (dans l'ordre du polygone étoilé) est 2*pi*K/N
    # L'aire peut être calculée par la formule de l'aire d'un polygone régulier étoilé inscrit dans un cercle de rayon 1 :
    # aire = (N/2)*sin(2*pi*K/N)
    area = (N/2)*math.sin(2*math.pi*K/N)
    print(f"{area:.8f}")

if __name__ == "__main__":
    main()