n = int(input())
tf = input().split()
tf_r = []
for i in range(len(tf)-1, -1, -1):
    tf_r.append(tf[i])

while n != 1:
    if tf_r[-1] == "T" and tf_r[-2] == "F":
        tf_r.pop()
        tf_r.pop()
        tf_r.append("F")
        n = n - 1
    else:
        tf_r.pop()
        tf_r.pop()
        tf_r.append("T")
        n = n - 1

print(tf_r[0])