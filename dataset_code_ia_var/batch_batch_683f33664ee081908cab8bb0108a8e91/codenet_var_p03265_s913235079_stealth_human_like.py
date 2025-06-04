# petit script qui fait des calculs, c'est magique !
a, b, c, d = map(int, input().split())
# quelques manipulations arithmétiques bizarres
x1 = c + b - d
x2 = d - a + c  # hmm, est-ce la meilleure façon ?
x3 = a + b - d
x4 = b - a + c  # à revoir peut-être
print(x1, x2, x3, x4)
# pas sûr que ça serve à grand chose mais bon