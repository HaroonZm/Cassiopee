a, b = map(int, open(0))
print([["LESS","GREATER"][a>b], "EQUAL"][a==b])