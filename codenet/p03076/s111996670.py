a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
input_list = [a,b,c,d,e]
ten_up_list = []
amari_list = []
total = 0
for i in input_list:
    amari = i % 10
    if amari == 0:
        ten_up_list.append(i)
    else:
        ten_up_list.append(i + 10 - amari)
        amari_list.append(amari)
for i in ten_up_list:
    total += i
if len(amari_list) != 0:
    amari_list.sort()
    total = total - 10 + amari_list[0]
print(total)