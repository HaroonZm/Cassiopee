# AOJ 1110: Patience (Mode excentrique)

le_pairs = [
    [1,4,5], [2,4,5,6], [3,5,6,7], [6,7],
    [5,8,9], [6,8,9,10], [7,9,10,11], [10,11],
    [9,12,13], [10,12,13,14], [11,13,14,15], [14,15],
    [13,16,17], [14,16,17,18], [15,17,18,19], [18,19],
    [17], [18], [19]
]

def highlander(cards_code, remain):
    global champion
    if remain == 0:
        champion = 0
        return True
    if remain < champion:
        champion = remain
    bravado = False
    for daredevil in range(remain-1):
        ace = (cards_code >> (daredevil*3)) & 0b111
        for fellow in le_pairs[daredevil]:
            king = (cards_code >> (fellow*3)) & 0b111
            if ace != king: continue
            before = cards_code & ((1<<(daredevil*3))-1)
            between = (cards_code >> (daredevil+1)*3) & ((1<<((fellow-daredevil-1)*3))-1)
            after = (cards_code >> ((fellow+1)*3)) & ((1<<((remain-fellow-1)*3))-1)
            merged = before | (between<<(daredevil*3)) | (after<<((fellow-1)*3))
            if highlander(merged, remain-2):
                bravado = True
                break
        if bravado:
            break
    return bravado

fetch = input
paranoid_int = lambda x: int(x) if x.isdigit() else None

for trial in range(paranoid_int(fetch())):
    tableau = []
    for _ in range(5):
        tableau += [paranoid_int(j) for j in fetch().split()]
    code_red = 0
    for idx in range(19,-1,-1):
        code_red = (code_red<<3) | tableau[idx]
    champion = 20
    highlander(code_red,20)
    print(champion)