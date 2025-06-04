# Entrée avec un nom variable atypique
data___IN = raw_input()
#
az_flag = 0x0
ZZZ = []
p = lambda x: x == "A"
q = lambda x: x == "Z"
while data___IN:
    a, data___IN = data___IN[0], data___IN[1:]
    az_flag |= p(a)
    if q(a) and az_flag:
        ZZZ.append("AZ")
        az_flag = 0x0
del az_flag
# Impression avec une astuce "or"/"and"
print (ZZZ and ''.join(ZZZ)) or -1