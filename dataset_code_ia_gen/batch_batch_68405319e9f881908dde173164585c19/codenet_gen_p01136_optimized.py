import sys
from collections import deque

def main():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        avail = [set() for _ in range(n)]
        for i in range(n):
            data = list(map(int, input().split()))
            for d in data[1:]:
                avail[i].add(d)

        # Each state: (possessed mask, day)
        # Initialize queue with each person alone on their available days
        # We want minimal day d (1<=d<=30) to have possessed == all people

        full = (1 << n) -1
        visited = [ [False]*31 for _ in range(1<<n) ]

        queue = deque()
        # Add initial states: one person with their map on each available day
        for i in range(n):
            for d in avail[i]:
                mask = 1 << i
                if not visited[mask][d]:
                    visited[mask][d] = True
                    queue.append( (mask,d) )

        res = -1
        while queue:
            mask, day = queue.popleft()
            if mask == full:
                if res == -1 or day < res:
                    res = day
                continue
            if day == 30:
                continue
            next_day = day + 1

            # For each person:
            # Persons in mask have the map fragments they possess
            # On next_day, people available that day
            # Transfer can happen among those available that day:
            # Map possession can be merged in one step (day),
            # since one can meet multiple people same day.

            # Find people available on next_day
            avail_next = [i for i in range(n) if next_day in avail[i]]
            if not avail_next:
                # no transfer possible; but day advances
                if not visited[mask][next_day]:
                    visited[mask][next_day] = True
                    queue.append( (mask, next_day) )
                continue

            # Among avail_next, who currently has map fragment?
            have_map = [i for i in avail_next if (mask & (1<<i)) !=0]
            if not have_map:
                # no map among today's available, can't spread; just advance day
                if not visited[mask][next_day]:
                    visited[mask][next_day] = True
                    queue.append( (mask, next_day) )
                continue

            # After gathering, all available on next_day will share maps of all those present with maps
            # So new mask is mask plus all avail_next
            new_mask = mask
            for i in avail_next:
                new_mask |= (1 << i)
            if not visited[new_mask][next_day]:
                visited[new_mask][next_day] = True
                queue.append( (new_mask, next_day) )

        print(res)

if __name__=="__main__":
    main()