import collections

while True:
    W, D = map(int, input().split())
    if W == 0 and D == 0:
        break
    
    hw = list(map(int, input().split())) # Hardware, je suppose
    hd = list(map(int, input().split())) # Software...?
    
    counter_hw = collections.Counter(hw)
    counter_hd = collections.Counter(hd)
    
    # Bon, on va faire deux calculs, pas complètement sûr que ce soit optimal mais ça marche
    somm1 = sum(hw)
    for k in counter_hd:
        if counter_hd[k] > counter_hw.get(k,0):
            somm1 += (counter_hd[k] - counter_hw.get(k,0)) * k
    
    somm2 = sum(hd)
    for k in counter_hw:
        if counter_hw[k] > counter_hd.get(k,0):
            somm2 += (counter_hw[k] - counter_hd.get(k,0)) * k

    # On affiche le plus petit des deux. Y a peut-être une façon plus élégante...
    print(min(somm1, somm2))