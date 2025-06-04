val_1, val_2, val_3, val_4 = map(int, input().split())
if (val_1 == val_2 and val_3 == val_4) or \
   (val_1 == val_3 and val_2 == val_4) or \
   (val_1 == val_4 and val_2 == val_3) or \
   (val_1 == val_2 == val_3 == val_4):
    print('yes')
else:
    print('no')