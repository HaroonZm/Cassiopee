def shredder(target, number):
    if int(number) == target:
        # Special case: no cut needed
        print(f"{target} {number}")
        return

    digits = number
    n = len(digits)

    best_sum = -1
    best_partitions = []
    memo = {}

    # dfs(pos, current_sum) returns all partitions from pos with sum <= target - current_sum
    # For performance, store only sets of partitions leading to max sum<=target
    def dfs(pos, current_sum):
        if pos == n:
            return { ((), 0) }  # set of tuples (partition tuple, sum)

        if (pos, current_sum) in memo:
            return memo[(pos, current_sum)]

        res = set()
        max_sum_found = -1

        for end in range(pos+1, n+1):
            part_str = digits[pos:end]
            if part_str[0] == '0':
                # Leading zero not allowed
                continue
            part_val = int(part_str)
            new_sum = current_sum + part_val
            if new_sum <= target:
                # Continue dfs
                next_partitions = dfs(end, new_sum)
                for partition, s in next_partitions:
                    total_sum = part_val + s
                    if total_sum > max_sum_found:
                        max_sum_found = total_sum
                        res = set()
                        res.add(((part_str,) + partition, total_sum))
                    elif total_sum == max_sum_found:
                        res.add(((part_str,) + partition, total_sum))
            else:
                # sum exceeded target
                continue

        memo[(pos, current_sum)] = res
        return res

    partitions = dfs(0,0)
    if not partitions:
        print('error')
        return

    # Get max sum from the found partitions
    max_sum = max(s for _, s in partitions)

    # Filter partitions with max_sum only
    max_partitions = [p for p,s in partitions if s == max_sum]

    if len(max_partitions) == 0:
        print('error')
        return
    if len(max_partitions) > 1:
        # Check if partitions are identical (only differing by representation?), consider order matters, if exactly the same partitions repeated, only one result. Else rejected.
        unique = set(max_partitions)
        if len(unique) > 1:
            print('rejected')
            return

    # else print the unique one
    parts = max_partitions[0]
    # compute the sum
    sum_parts = sum(int(p) for p in parts)
    print(str(sum_parts) + ' ' + ' '.join(parts))


while True:
    line = input().strip()
    if line == '0 0':
        break
    t, num = line.split()
    t = int(t)
    shredder(t,num)