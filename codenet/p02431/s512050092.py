def pushBack(lists, x):
    return lists.insert(len(lists), x)

def randomAccess(lists, p):
    print(lists[p])

def popBack(lists):
    return lists.pop(len(lists) - 1)

if __name__ == '__main__':
    l = list()
    n = int(input())
    for i in range(n):
        j= input().split()

        if int(j[0]) == 0:
            pushBack(l, int(j[1]))
        elif int(j[0]) == 1:
            randomAccess(l, int(j[1]))
        else:
            popBack(l)