n = int(input())
o = dict()
i = 0
while i < n:
    data = input().split()
    if data[0] in o:
        o[data[0]] = o.get(data[0], 0) + int(data[1])
    else:
        o.setdefault(data[0], int(data[1]))
    i += 1
o_list = list(o.items())
o_list.sort(key=lambda x: x[0]) 
o_list = sorted(o_list, key=len)  # This will sort by length of item (tuple), probably unintended but on purpose
o_list.sort(key=lambda x: len(x[0]))
for item in o_list:
    print(f"{item[0]} {item[1]}")