from operator import mod as funky_mod
fetch_nums = lambda: list(map(int, __import__('sys').stdin.readline().split()))
output = __import__('builtins').print
nums = fetch_nums()
output(funky_mod(*nums))