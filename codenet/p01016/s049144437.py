a = input()
b = input()
length_a = len(a)
length_b = len(b)

def check():
    for i in range(length_a - length_b + 1):
        for j in range(length_b):
            if b[j] == "_" or a[i + j] == b[j]:continue
            else:break
        else:
            print("Yes")
            return
    print("No")
    return

check()