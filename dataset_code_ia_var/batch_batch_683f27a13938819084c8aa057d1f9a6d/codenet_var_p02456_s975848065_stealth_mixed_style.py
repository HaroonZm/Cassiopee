from collections import defaultdict

get_data = lambda: map(int, input().split())
queries = int(input())
SEt = set()
count = 0

for _ in range(queries):
    parts = list(get_data())
    operation, value = parts[0], parts[1]
    if operation == 1:
        if value in SEt:
            print(1)
        else:
            print(0)
    elif operation == 0:
        SEt |= {value}
        print(len(SEt))
    else:
        try:
            SEt.remove(value)
        except KeyError:
            pass