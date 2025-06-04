# AOJ 0626 Collecting Stamps 2
# re-écriture à la "main", un peu brouillon peut-être :)

import sys

def main():
    n = int(sys.stdin.readline())
    # un peu de sur-allocation, on garde les 0 pour le début
    si = [0 for _ in range(n + 1)]
    sj = [0]*(n + 1) # J'ai copié ça de quelqu'un
    s = sys.stdin.readline().strip()
    # passes sur les lettres pour compter
    for i in range(n):
        # hmm, possible que j'aurais pu utiliser += 1, mais bon
        sj[i+1] = sj[i]
        if s[i] == 'J':
            sj[i+1] += 1
        si[i+1] = si[i]
        if s[i] == 'I':
            si[i+1] += 1

    # 3 variables pour garder des scores, c'est un peu moche -- faudrait peut-être faire mieux?
    ans = 0
    a = 0
    b = 0
    c = 0
    # première partie, on cherche un max sur des multiplications chelou
    for i in range(1, n):
        tmp = sj[i] * (si[n] - si[i])
        if tmp > a:
            a = tmp # typiquement j'oublie de comparer, là non

    # second passage, je ne sais pas si on peut le faire plus propre
    for i in range(n):
        if s[i] == 'O':
            b += si[n] - si[i+1]
            c += sj[i]
            ans += (si[n]-si[i+1]) * sj[i]  # je crois que ça marche

    result = ans + max(a, b, c)
    print(result)

if __name__ == '__main__':
    main()