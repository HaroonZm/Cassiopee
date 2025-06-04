a, b, c, l_list = 0, 0, 0, []

nac = input().split()
n = int(nac[0])
a = int(nac[1])
b = int(nac[2])
c = int(nac[3])
l_list = []
for _ in range(n):
    l_list.append(int(input()))

stack = []
stack.append((0, 0, 0, 0))
best = 1 << 20

while stack:
    l_key, a_sum, b_sum, c_sum = stack.pop()
    if l_key == len(l_list):
        if min(a_sum, b_sum, c_sum) > 0:
            cost = abs(a - a_sum) + abs(b - b_sum) + abs(c - c_sum) - 30
            if cost < best:
                best = cost
        continue
    l_value = l_list[l_key]
    # Pass (don't use this item)
    stack.append((l_key + 1, a_sum, b_sum, c_sum))
    # Use for a
    stack.append((l_key + 1, a_sum + l_value, b_sum, c_sum))
    # Note: We'll need to manage the +10 penalty
    # Use for b
    stack.append((l_key + 1, a_sum, b_sum + l_value, c_sum))
    # Use for c
    stack.append((l_key + 1, a_sum, b_sum, c_sum + l_value))

# Now, have to re-calculate the penalties for combinations that used resources (should count +10 each time except for first use)
# To implement the penalty, instead of recalculating, keep track of number of assigned rods and add 10 * (assigned rods - 3)

stack2 = []
stack2.append((0, 0, 0, 0, 0)) # l_key, a_sum, b_sum, c_sum, cnt (count of assigned)

ans = 1 << 20
while stack2:
    l_key, a_sum, b_sum, c_sum, cnt = stack2.pop()
    if l_key == len(l_list):
        if min(a_sum, b_sum, c_sum) > 0:
            cost = abs(a - a_sum) + abs(b - b_sum) + abs(c - c_sum) + (cnt - 3) * 10
            if cost < ans:
                ans = cost
        continue
    l_value = l_list[l_key]
    # Don't use this item
    stack2.append((l_key + 1, a_sum, b_sum, c_sum, cnt))
    # Use for a
    stack2.append((l_key + 1, a_sum + l_value, b_sum, c_sum, cnt + 1))
    # Use for b
    stack2.append((l_key + 1, a_sum, b_sum + l_value, c_sum, cnt + 1))
    # Use for c
    stack2.append((l_key + 1, a_sum, b_sum, c_sum + l_value, cnt + 1))

print(ans)