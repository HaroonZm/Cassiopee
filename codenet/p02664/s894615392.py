T = input()
l = list(T)
l_replace = ["D" if i == "?" else i for i in l]
print(''.join(l_replace))