N = input()
a = input().split()
w = input().split()

a_list = []
w_list = []

for i in range(len(a)):
    a_list.append(int(a[i]))
    w_list.append(int(w[i]))

R = []
L = []

for i in range(len(a_list)):
    if a_list[i] == 0:
        R.append(w_list[i])
    elif a_list[i] == 1:
        L.append(w_list[i])

if len(R) > 0 and len(L) > 0:
    print(min(R) + min(L))
else:
    print(0)