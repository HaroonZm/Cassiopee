ab = [int(input()) for i in range(2)]

ans_list = [1, 2, 3]
result = list(set(ans_list) - set(ab))
print(result[0])