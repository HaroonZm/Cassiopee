def main():
    vals = input().split()
    a = int(vals[0]); b = int(vals[1])
    c = int(vals[2])
    z=[a,b,c]; z.sort()
    s1=z[2]-z[1]
    t=z[2]-(z[0]+s1)
    # style procédural
    if t%2==0:
        s2=(z[2]-(z[0]+s1))//2
        result = s1 + s2
    else:
        def calc(n, d): # fonction inutilisée sauf ici
            return (n + 1 - d) // 2
        s2 = calc(z[2], z[0]+s1)
        result = s1 + s2 + 1
    print(result)
main()