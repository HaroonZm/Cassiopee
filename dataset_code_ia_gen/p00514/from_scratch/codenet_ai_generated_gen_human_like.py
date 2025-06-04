from math import comb

def main():
    n, m, r = map(int, input().split())
    # On cherche le nombre de combinaisons (k1,...,kn) avec ki >= m et sum ki = r
    # Cela revient à chercher les compositions de r - n*m en n parties >= 0
    # Donc nombre de combinaisons = comb(r - n*m + n -1, n -1) si r >= n*m, sinon 0
    rem = r - n * m
    if rem < 0:
        print(0)
        return
    # comb avec r >= n*m >=0
    res = comb(rem + n -1, n -1)
    print(res)

if __name__ == "__main__":
    main()