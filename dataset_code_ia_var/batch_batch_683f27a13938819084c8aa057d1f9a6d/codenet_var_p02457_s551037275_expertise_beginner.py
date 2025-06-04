import sys

my_set = set()
_ = input()

for line in sys.stdin:
    parts = line.strip().split()
    command = parts[0]

    if command == '0':
        num = int(parts[1])
        my_set.add(num)
        print(len(my_set))
    elif command == '1':
        num = int(parts[1])
        if num in my_set:
            print(1)
        else:
            print(0)
    elif command == '2':
        num = int(parts[1])
        if num in my_set:
            my_set.remove(num)
    else:
        left = int(parts[1])
        right = int(parts[2])
        nums_in_range = []
        for n in my_set:
            if left <= n <= right:
                nums_in_range.append(n)
        nums_in_range.sort()
        for n in nums_in_range:
            print(n)