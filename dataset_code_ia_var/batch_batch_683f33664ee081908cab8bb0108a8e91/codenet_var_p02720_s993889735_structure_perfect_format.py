import queue

def strtoNum(l):
    val = ''
    for _ in l:
        val += _
    return int(val)

k = int(input())

if k < 10:
    print(k)
    exit()

lun = queue.Queue()
for i in range(1, 10):
    lun.put(i)

cnt = 9
apdNum = [
    [0, 1],
    [0, 1, 2],
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7],
    [6, 7, 8],
    [7, 8, 9],
    [8, 9]
]

while not lun.empty():
    getNum = list(str(lun.get()))
    chkNum = int(getNum[-1])
    for i in apdNum[chkNum]:
        cnt += 1
        putNum = getNum + [str(i)]
        if cnt == k:
            print(strtoNum(putNum))
            exit()
        else:
            lun.put(strtoNum(putNum))