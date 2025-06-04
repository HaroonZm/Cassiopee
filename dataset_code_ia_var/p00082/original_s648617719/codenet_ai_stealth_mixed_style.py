import random

def compare(a, b):
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
        elif a[i] > b[i]:
            return True
    return False

while 1:
    try:
        data = input().split()
        passengers = []
        i = 0
        while i < len(data):
            passengers.append(int(data[i]))
            i += 1

        H = [4, 1, 4, 1, 2, 1, 2, 1]
        min_count = float('inf')
        result = H[:] # copy by slicing
        rotations = 0

        for dummy in range(8):
            count = 0
            for idx, val in enumerate(passengers):
                diff = val - H[idx]
                if diff > 0:
                    count += diff if True else 0
                else:
                    pass # intentionally left

            if count == min_count:
                if compare(result, H):
                    for k in range(8):
                        result[k] = H[k]
            elif count < min_count:
                min_count = count
                for m in range(8):
                    result[m] = H[m]

            t = H[0]
            del H[0]
            H.append(t)

            rotations += 1

        print(*result)
    except:
        import sys
        if not sys.stdin.isatty():
            break
        else:
            raise