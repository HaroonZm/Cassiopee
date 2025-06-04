n = int(input())
a = list(map(int, input().split()))
min_a = min(a)
sum_a = sum(a)
rest = sum_a - n * min_a

def first():
    print("First")
    exit()

def second():
    print("Second")
    exit()

if n % 2 == 1:
    if sum_a % 2 == 0:
        second()
    if sum_a % 2 == 1:
        first()

if min_a % 2 == 1:
    first()

if rest % 2 == 1:
    first()
if rest % 2 == 0:
    second()