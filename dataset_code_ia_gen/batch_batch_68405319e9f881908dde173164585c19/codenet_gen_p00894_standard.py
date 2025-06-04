def to_minutes(date_str, time_str):
    month, day = map(int, date_str.split('/'))
    hour, minute = map(int, time_str.split(':'))
    return ((month * 31 + day) * 24 + hour) * 60 + minute

while True:
    n = int(input())
    if n == 0:
        break
    logs = [input().split() for _ in range(n)]

    inside = set()
    goddess_present = False
    last_time = 0
    blessed_time = {}
    active_programmers = set()

    for i in range(n):
        date, time, event, pid = logs[i]
        current_time = to_minutes(date, time)

        duration = current_time - last_time
        if goddess_present:
            for p in inside:
                if p != '000':
                    blessed_time[p] = blessed_time.get(p, 0) + duration

        if event == 'I':
            inside.add(pid)
            if pid == '000':
                goddess_present = True
        else:
            inside.remove(pid)
            if pid == '000':
                goddess_present = False

        last_time = current_time

    print(max(blessed_time.values()) if blessed_time else 0)