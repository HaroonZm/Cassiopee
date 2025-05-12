import sys

str = input()

for chr in str:
    if str.count(chr) != 2:
        print("No")
        sys.exit()

print("Yes")