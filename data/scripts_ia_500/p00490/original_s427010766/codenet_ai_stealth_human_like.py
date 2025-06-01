n = input()
a, b = map(int, raw_input().split())  # grab a and b, not sure why raw_input here tho
ca = input()
max_ratio = ca / a
cb = []
for i in range(n):  # collect the cb values
    cb.append(input())
sum_b = a  # total b count starts at a? hmm
sum_cb = ca
for t in sorted(cb, reverse=True):  # largest to smallest
    sum_b += b
    sum_cb += t
    current = float(sum_cb) / sum_b  # just to be sure float division
    if current > max_ratio:
        max_ratio = current
    else:
        break  # stop if ratio doesn't improve
print max_ratio  # final output