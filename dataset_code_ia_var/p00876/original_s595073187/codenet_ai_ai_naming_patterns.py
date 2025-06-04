from collections import deque

while True:
    task_count = int(input())
    if task_count == 0:
        break

    task_times = [0] * task_count
    task_cycles = [0] * task_count
    queue_inactive = deque()
    queue_active = deque()
    task_properties = [list(map(int, input().split())) for _ in range(task_count)]
    task_properties.sort()
    for idx in range(task_count):
        time_required, cycles = task_properties[idx]
        queue_inactive.append((idx, time_required))
        task_times[idx] = time_required
        task_cycles[idx] = cycles

    max_time = 0
    tasks_remaining = task_count
    INF = 10 ** 18

    while tasks_remaining:
        current_time = min(queue_inactive[0][1] if queue_inactive else INF,
                           queue_active[0][1] if queue_active else INF)
        ready_inactive = []
        ready_active = []

        while queue_inactive and queue_inactive[0][1] <= current_time:
            ready_inactive.append(queue_inactive.popleft()[0])
        ready_inactive.sort()
        for idx in ready_inactive:
            queue_active.append((idx, current_time + task_times[idx]))

        while queue_active and queue_active[0][1] <= current_time:
            ready_active.append(queue_active.popleft()[0])
        ready_active.sort()
        for idx in ready_active:
            if task_cycles[idx] == 1:
                tasks_remaining -= 1
            else:
                queue_inactive.append((idx, current_time + task_times[idx]))
            task_cycles[idx] -= 1

        max_time = max(max_time, current_time)
    print(max_time)