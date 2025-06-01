a,b,c,d = map(int, input().split())
print('yes' if len({a,b,c,d}) < 4 and any({a,b} == pair for pair in [{b,c}, {c,d}, {d,a}]) or a==b==c==d else 'no')