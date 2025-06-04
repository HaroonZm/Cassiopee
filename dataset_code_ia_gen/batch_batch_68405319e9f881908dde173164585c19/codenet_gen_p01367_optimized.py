import sys
import heapq

input = sys.stdin.readline

def can_finish(N, T, customers, ops):
    events = []  # (time, 0:start call, 1:end call)
    waiting = []  # waiting customers by id
    call_times = [0]*N
    standbys = [0]*N
    call_indexes = [0]*N  # count of calls started for each customer
    for i in range(N):
        heapq.heappush(events, (0, 0, i))
    busy = 0
    ready_ops = ops
    call_heap = []  # (id, customer)
    wait_queue = []  # (id, customer), for priority of waiting customers by id

    while events:
        t, etype, cid = heapq.heappop(events)
        if t > T:
            return False

        if etype == 1:  # call ended
            busy -= 1
            ready_ops += 1
            # immediately assign waiting customers if any
            while ready_ops > 0 and wait_queue:
                wcid = wait_queue[0][1]
                wl, wcid = wait_queue[0]
                if wl < t:
                    # timeout while waiting, remove and enqueue next call
                    heapq.heappop(wait_queue)
                    ncall = t + customers[wcid][2]
                    if ncall <= T:
                        heapq.heappush(events, (ncall, 0, wcid))
                    continue
                heapq.heappop(wait_queue)
                ready_ops -= 1
                busy += 1
                endt = t + customers[wcid][0]
                if endt > T:
                    return False
                heapq.heappush(events, (endt, 1, wcid))
        else:
            # start call event
            if ready_ops > 0:
                ready_ops -= 1
                busy += 1
                endt = t + customers[cid][0]
                if endt > T:
                    return False
                heapq.heappush(events, (endt, 1, cid))
            else:
                # add to wait queue with (expire_time, id)
                expire = t + customers[cid][1]
                heapq.heappush(wait_queue, (expire, cid))
    return True

def min_operators(N, T, customers):
    left, right = 1, N
    while left < right:
        mid = (left+right)//2
        if can_finish(N, T, customers, mid):
            right = mid
        else:
            left = mid+1
    return left

while True:
    N,T = map(int,input().split())
    if N==0 and T==0:
        break
    customers = [tuple(map(int,input().split())) for _ in range(N)]
    print(min_operators(N,T,customers))