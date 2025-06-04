import collections
import sys

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_int_list_minus1():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def read_float_list():
    return [float(x) for x in sys.stdin.readline().split()]

def read_string_list():
    return sys.stdin.readline().split()

def read_int():
    return int(sys.stdin.readline())

def read_float():
    return float(sys.stdin.readline())

def read_string():
    return input()

def print_flush(s):
    print(s, flush=True)

def main():
    result = []
    while True:
        n = read_int()
        if n == 0:
            break
        entries = []
        for _ in range(n):
            parts = read_string_list()
            entries.append(parts)
        last_time = {}
        total_time = collections.defaultdict(int)
        for entry in entries:
            day = entry[0]
            ts = entry[1]
            flag = entry[2]
            idx = int(entry[3])
            h,m = map(int, ts.split(':'))
            minutes = h*60 + m
            if idx == 0:
                if flag == 'I':
                    for k in list(last_time.keys()):
                        total_time[k] -= minutes - last_time[k]
                    last_time[idx] = minutes
                else:
                    del last_time[idx]
                    for k in list(last_time.keys()):
                        total_time[k] += minutes - last_time[k]
            else:
                if flag == 'I':
                    last_time[idx] = minutes
                else:
                    if 0 in last_time:
                        total_time[idx] += minutes - last_time[idx]
                    if idx in last_time:
                        del last_time[idx]
        if len(total_time) == 0:
            result.append(0)
        else:
            result.append(max(total_time.values()))
    return '\n'.join(str(x) for x in result)

print(main())