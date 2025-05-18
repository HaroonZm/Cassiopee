s = input()

#ans = 'Yes' if\
#    s.count('a') == 1 and \
#    s.count('b') == 1 and \
#    s.count('c') == 1 else 'No'

abc = 'abc'
ans = 'Yes' if 3 == sum(1 if s.count(c)==1 else 0 for c in abc ) else 'No'

print( ans )