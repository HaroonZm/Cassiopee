val_int_first, val_int_second = map(int, raw_input().split())
if val_int_first > val_int_second:
    print "val_int_first > val_int_second"
elif val_int_first < val_int_second:
    print "val_int_first < val_int_second"
elif val_int_first == val_int_second:
    print "val_int_first == val_int_second"