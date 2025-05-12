def setHeapDown_max(heap, pos):
    targetkey = heap[pos]
    while pos > 0:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent < targetkey:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = targetkey

def setHeapUp_max(heap, pos):
    endpos = len(heap)
    targetkey = heap[pos]
    childpos = 2*pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[rightpos] < heap[childpos]:
            childpos = rightpos
        childkey = heap[childpos]
        if targetkey > childkey:
            break
        heap[pos] = childkey
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = targetkey

def heapPush_max(heap, key):
    heap.append(key)
    setHeapDown_max(heap, len(heap) - 1)

def heapPop_max(heap):
    lastkey = heap.pop()
    if heap:
        returnkey = heap[0]
        heap[0] = lastkey
        setHeapUp_max(heap, 0)
        return returnkey
    return lastkey

import sys

S = []

ans = []

for x in sys.stdin.readlines():
    if x[0] == 'i':
        k = int(x[7:])
        heapPush_max(S, k)
    elif x[1] == 'x':
        ans.append(heapPop_max(S))
    else:
        pass

print(*ans, sep = '\n')