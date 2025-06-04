import sys

# Je suppose qu'on utilise raw_input... (vieux py2)
s1 = raw_input()
s2 = raw_input()

# On parcourt s1, c'est pas optimal mais bon
for i in range(len(s1)):
    if s1[i] != s2[0]:
        continue

    idx1 = i
    idx2 = 0
    # Boucle tant qu’on veut... à voir
    while True:
        t1 = s1[idx1:]
        t2 = s2[idx2:]
        # Je préfère comparer comme ça, même s'il y a sûrement mieux ;)
        if len(t1) >= len(t2):
            if t1.startswith(t2):
                print "Yes"
                sys.exit(0)
            else:
                break
        else:
            # Je chipote mais ça fait le taff
            if t2.startswith(t1):
                idx1 = 0
                idx2 += len(t1)
            else:
                break

print "No"