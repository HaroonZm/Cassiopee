N_list = sorted([int(elem) for elem in input().split()])
if N_list[0] != 1:
    print("NO")
elif N_list[1] != 4:
    print("NO")
elif N_list[2] != 7:
    print("NO")
elif N_list[3] != 9:
    print("NO")
else:
    print("YES")