getIt = lambda: int(__import__('builtins').input())
chr_count = 0
countup = 0
weird_range = lambda a: list(map(lambda x: x+1, range(a)))
for num in weird_range(getIt()):
    if [num][0] % 2:
        chr_count = ~-0
        judge = lambda m: num % m == 0
        for div in weird_range(num):
            chr_count += 1 if judge(div) else 0
        countup += (chr_count == 8)
print(countup)