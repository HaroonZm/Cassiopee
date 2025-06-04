N = int(input())
ladder_mappings = []

for _ in range(N):
    data = list(map(int, input().split()))
    w = data[0]
    a = data[1:]
    
    pos = [0, 1, 2]  # initial positions of left(0), center(1), right(2)
    # For each horizontal line, swap positions accordingly
    # Horizontal line connects center to left or center to right at that step
    for direction in a:
        if direction == 0:
            # swap center and left
            pos[0], pos[1] = pos[1], pos[0]
        else:
            # swap center and right
            pos[1], pos[2] = pos[2], pos[1]
    ladder_mappings.append(pos)

# For each ladder, create a mapping from starting line to ending line
# For lines 0,1,2, find where they end after the ladder
mappings = []
for pos in ladder_mappings:
    m = [0, 0, 0]
    for i in range(3):
        # pos contains final positions, but indices represent original positions,
        # so we need to find the final position of each starting point i.
        # Since pos array after swapping tells final position of line i at index i,
        # we can interpret pos[i] as line currently at position i.
        # But we want a mapping from start line to end line.
        # Actually pos[i] tells the label at position i after shuffles.
        # So it's reversed: For start line s, find the position p so that pos[p] = s
        # So invert the mapping:
        # For start line i, find where it ended:
        # pos is final order of lines at positions 0,1,2, so pos[p] is line at position p
        # For start line i, find p with pos[p] == i, then end line is p
        # So m[i] = p where pos[p] == i
        for p in range(3):
            if pos[p] == i:
                m[i] = p
                break
    mappings.append(m)

# Now, we can choose any subset of ladders (at least one), in any order to connect vertically
# We want to see if there is a sequence of ladders whose composite mapping is identity:
# for all line i, after applying all ladders in sequence, end line == start line
# Identity mapping is [0,1,2]

from itertools import product

# Because N could be up to 50, all subsets is huge. We'll try all permutations with repetition is impossible.

# Instead, we try all combinations with length 1 to N (because order matters), it's huge.

# We'll try all permutations of length 1 to N but that is too large.

# We need a simple approach: since the number of possible mappings from 3 lines to 3 lines is small (3! = 6),
# we can use BFS on mappings to see if identity is reachable.

identity = [0, 1, 2]
seen = set()
from collections import deque

queue = deque()

# start from all ladders as possible starting composite mappings
for m in mappings:
    t = tuple(m)
    queue.append(t)
    seen.add(t)

found = False
while queue:
    current = queue.popleft()
    if list(current) == identity:
        found = True
        break
    # compose current with all ladders
    for m in mappings:
        # compose m after current:
        # composition: (m o current)[i] = m[current[i]]
        new_mapping = [m[current[i]] for i in range(3)]
        t_new = tuple(new_mapping)
        if t_new not in seen:
            seen.add(t_new)
            queue.append(t_new)

print("yes" if found else "no")