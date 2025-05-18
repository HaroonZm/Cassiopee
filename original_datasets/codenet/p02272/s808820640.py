cnt = 0
def merge_sort(array):
    global cnt
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    cnt += len(left) + len(right)
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    list = []
    l_index, r_index = 0, 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            list.append(left[l_index])
            l_index += 1
        else:
            list.append(right[r_index])
            r_index += 1
    if l_index < len(left):
        list.extend(left[l_index:])
    if r_index < len(right):
        list.extend(right[r_index:])
    
    return list

n = int(input())
S = list(map(int, input().split()))
array = merge_sort(S)
print(" ".join(map(str, array)))
print(cnt)