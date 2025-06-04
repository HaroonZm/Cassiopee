n = int(input())
result_dict = {}
for i in range(n):
    string = input()
    result_dict[string] = 1
print(len(result_dict.keys()))