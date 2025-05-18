n = str(input())

hon = [2, 4, 5, 7, 9]
pon = [0, 1, 6, 8]
bon = 3

a = n[-1]

if int(a) in hon:
    print('hon')
elif int(a) in pon:
    print('pon')
elif int(a) == 3:
    print('bon')