import sys
import heapq

input = sys.stdin.readline

def can_finish(ops, customers, T):
    # ops: number of operators
    # customers: list of (M, L, K)
    # T: time limit

    # Each operator available time
    operators = [0]*ops
    heapq.heapify(operators)

    # Event queue: (time, customer_id, action)
    # action: 0 for call attempt
    # We'll manage calls by simulating customers calling, waiting and retrying
    # For each customer, store the next call time
    calls = []
    for i, (M, L, K) in enumerate(customers):
        # All call at time 0 intially, push (call_time, customer_id)
        heapq.heappush(calls, (0, i))

    # For each customer, we need to track if done
    done = [False]*len(customers)

    # Priority queue for waiting customers: (id, call_time, deadline, M, L, K)
    waiting = []

    current_time = 0

    while calls or waiting:
        # Pick earliest event time from calls or waiting
        next_call_time = calls[0][0] if calls else float('inf')
        next_op_free = operators[0] if operators else float('inf')

        current_time = min(next_call_time, next_op_free)

        # Move waiting callers who timeout at current_time and schedule retry if needed
        new_waiting = []
        while waiting:
            cid, call_t, deadline, M, L, K = heapq.heappop(waiting)
            # If call timed out before current_time, retry call after K time units
            # If they still have not been assigned and waiting too long, schedule retry
            if deadline <= current_time:
                # The caller hung up at deadline, will retry at deadline+K if not done
                if not done[cid]:
                    next_call = deadline + K
                    if next_call <= T:
                        heapq.heappush(calls, (next_call, cid))
                # else done no retry
            else:
                # Still waiting, push back
                heapq.heappush(new_waiting, (cid, call_t, deadline, M, L, K))
        waiting = new_waiting

        # Assign operators who are free at current_time to waiting callers if any
        while operators and operators[0] <= current_time and waiting:
            op_free = heapq.heappop(operators)
            cid, call_t, deadline, M, L, K = heapq.heappop(waiting)
            # Check if call is still valid
            if deadline < current_time:
                # Client hung up, push retry call if in time
                if not done[cid]:
                    next_call = deadline + K
                    if next_call <= T:
                        heapq.heappush(calls, (next_call, cid))
                continue
            # Assign this operator to client -> operator busy until current_time+M
            done[cid] = True
            free_at = current_time + M
            if free_at > T:
                # Over time limit
                return False
            heapq.heappush(operators, free_at)

        # Now process all calls at current_time
        while calls and calls[0][0] == current_time:
            _, cid = heapq.heappop(calls)
            if done[cid]:
                continue
            M, L, K = customers[cid]
            # Add to waiting with deadline = current_time + L
            deadline = current_time + L
            heapq.heappush(waiting, (cid, current_time, deadline, M, L, K))

        # If no calls or waiting, jump to next event
        if not calls and waiting:
            # jump to soonest operator free or earliest waiting deadline
            next_deadline = min(w[2] for w in waiting)
            next_op_free = operators[0] if operators else float('inf')
            current_time = min(next_deadline, next_op_free)
            # can loop continue

    return all(done)

def main():
    while True:
        line = input()
        if not line:
            break
        N, T = map(int, line.split())
        if N == 0 and T == 0:
            break
        customers = []
        for _ in range(N):
            M, L, K = map(int, input().split())
            customers.append((M,L,K))
        # Binary search on number of operators
        left, right = 1, N
        res = N
        while left <= right:
            mid = (left + right)//2
            if can_finish(mid, customers, T):
                res = mid
                right = mid -1
            else:
                left = mid +1
        print(res)

if __name__ == "__main__":
    main()