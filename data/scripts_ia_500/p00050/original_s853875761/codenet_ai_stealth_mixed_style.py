def swap_fruits(s):
    lst = s.split()
    for i in range(len(lst)):
        if lst[i] == "apple":
            lst[i] = "kunimatsu"
    s1 = " ".join(lst)

    s1 = s1.replace("peach","apple")

    new_lst = list(s1)
    i = 0
    while i < len(new_lst):
        if ''.join(new_lst[i:i+9]) == "kunimatsu":
            new_lst[i:i+9] = list("peach")
            i += 5
        else:
            i += 1
    return ''.join(new_lst)

L = input()
print(swap_fruits(L))