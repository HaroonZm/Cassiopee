while True:
    n = int(input())
    if n == 0:
        break
    applications = []
    for _ in range(n):
        i, j, w = map(int, input().split())
        applications.append((i, j, w))
    # Sort applications by earliest start day
    applications.sort(key=lambda x: x[0])

    # We have two rooms, each day can be used by one concert at most
    # We'll try a simple greedy + backtracking approach with pruning visits.

    # Represent the schedule of days for each room as list of booleans
    # It's 1-based days 1 to 365
    # For beginner approach, try backtracking with simple pruning

    max_income = 0

    def can_place(room, start, end):
        for d in range(start, end + 1):
            if room[d]:
                return False
        return True

    def place(room, start, end):
        for d in range(start, end + 1):
            room[d] = True

    def remove(room, start, end):
        for d in range(start, end + 1):
            room[d] = False

    def backtrack(index, income, room1, room2):
        nonlocal max_income
        if index == n:
            if income > max_income:
                max_income = income
            return
        i, j, w = applications[index]
        # Option 1: skip this application
        backtrack(index+1, income, room1, room2)
        # Option 2: try to place in room1 if possible
        if can_place(room1, i, j):
            place(room1, i, j)
            backtrack(index+1, income + w, room1, room2)
            remove(room1, i, j)
        # Option 3: try to place in room2 if possible
        if can_place(room2, i, j):
            place(room2, i, j)
            backtrack(index+1, income + w, room1, room2)
            remove(room2, i, j)

    room1 = [False]* (366)
    room2 = [False]* (366)
    backtrack(0,0,room1,room2)
    print(max_income)