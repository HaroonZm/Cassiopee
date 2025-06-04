val_entree_1, val_entree_2 = map(int, raw_input().split())

if val_entree_1 < val_entree_2:
    print "val_entree_1 < val_entree_2"
elif val_entree_1 > val_entree_2:
    print "val_entree_1 > val_entree_2"
elif val_entree_1 == val_entree_2:
    print "val_entree_1 == val_entree_2"