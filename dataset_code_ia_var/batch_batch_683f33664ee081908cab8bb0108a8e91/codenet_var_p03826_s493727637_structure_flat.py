a_b_c_d = input().split()
a = int(a_b_c_d[0])
b = int(a_b_c_d[1])
c = int(a_b_c_d[2])
d = int(a_b_c_d[3])
prod1 = a * b
prod2 = c * d
if prod1 > prod2:
    result = prod1
else:
    result = prod2
print(result)