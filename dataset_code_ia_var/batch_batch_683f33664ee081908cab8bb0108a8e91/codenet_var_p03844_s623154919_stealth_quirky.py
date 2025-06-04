# Code Python réécrit avec des choix de conception non-conventionnels

exec('r=S:=input()\nL = S.split()\nx=[int,L[0].__int__][L[0].isdigit()]()\ny=[int,L[2].__int__][L[2].isdigit()]()\nq={"+" : lambda:_:x+y, "-" : lambda:_:x-y}.get(L[1],lambda:_:None)(None)\nprint(q)')