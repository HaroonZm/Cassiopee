s = input()
print((lambda w: ''.join([w, 'es']) if w.__getitem__(-1).__eq__('s') else ''.join([w, 's']))(s))