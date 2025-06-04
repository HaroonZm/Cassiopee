num_S = int(input())
list_S = input().split()
list_S = [int(element_S) for element_S in list_S]

num_T = int(input())
list_T = input().split()
list_T = [int(element_T) for element_T in list_T]

def search_linear(current_key):
    index_S = 0
    while list_S[index_S] != current_key:
        index_S += 1
        if index_S == num_S:
            return 0
    return 1

count_match = 0

for index_T in range(num_T):
    list_S.append(0)
    list_S[num_S] = list_T[index_T]
    count_match += search_linear(list_S[num_S])
print(count_match)