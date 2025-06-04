p, r, t = map(int, input().split())
available = list(map(int, input().split()))
need = [list(map(int, input().split())) for _ in range(p)]

# Tracking allocated resources per process
allocated = [[0]*r for _ in range(p)]

# Track number of acquired instances per process per resource during the log processing
# For performance, track remaining need per process per resource
remaining_need = [need[i][:] for i in range(p)]

# Count of finished processes
finished = [False]*p

def can_finish(process):
    for j in range(r):
        if remaining_need[process][j] > available[j]:
            return False
    return True

finished_count = 0
deadlock_unavoidable_time = -1

for time in range(1, t+1):
    proc, res = map(int, input().split())
    proc -= 1
    res -= 1

    # Process proc acquires one instance of resource res
    allocated[proc][res] += 1
    remaining_need[proc][res] -= 1
    available[res] -= 1

    # Check if any processes can finish now (repeat until fixpoint)
    progress = True
    while progress:
        progress = False
        for i in range(p):
            if not finished[i] and can_finish(i):
                # Process i can finish: release all allocated resources
                finished[i] = True
                finished_count += 1
                for j in range(r):
                    available[j] += allocated[i][j]
                    allocated[i][j] = 0
                progress = True

    # If not all processes done, check if no further progress possible (deadlock unavoidable)
    if finished_count < p:
        # For all un-finished processes, if none can finish under current available => deadlock unavoidable
        deadlock = True
        for i in range(p):
            if not finished[i] and can_finish(i):
                deadlock = False
                break
        if deadlock:
            deadlock_unavoidable_time = time
            break

print(deadlock_unavoidable_time)