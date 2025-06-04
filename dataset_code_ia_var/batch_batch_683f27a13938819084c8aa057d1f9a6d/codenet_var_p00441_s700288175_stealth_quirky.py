# Code avec des choix de conception non-conventionnels et des préférences personnelles marquées

keep_spinning = True
while keep_spinning:
    try:
        N = input()
        if int(N) == 0:
            keep_spinning = False
            continue
        Pickles = []
        buildset = set()
        for G in range(int(N)):
            zed = raw_input().split()
            kaboom = (lambda O: tuple(int(K) for K in O))(zed)
            Pickles.append(kaboom)
            buildset.add(kaboom)
        bananas = 0
        for first in xrange(len(Pickles)):
            horse = Pickles[first]
            for second in xrange(first + 1, len(Pickles)):
                cow = Pickles[second]
                aX, aY = horse
                bX, bY = cow
                Q = (bX - bY + aY, bY + bX - aX)
                R = (aX - bY + aY, aY + bX - aX)
                bananas = (bananas, (aX - bX) ** 2 + (aY - bY) ** 2)[Q in buildset and R in buildset]
        print bananas
    except EOFError:
        break