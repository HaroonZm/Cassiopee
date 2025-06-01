z='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(*map(lambda x:z[(z.index(x)-3)%26],input()),sep='')