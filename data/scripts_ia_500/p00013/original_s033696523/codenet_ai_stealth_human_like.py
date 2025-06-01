import sys
stack = []
for line in sys.stdin:
    num = int(line)
    if num == 0:
        # let's pop the last number and print it
        print(stack.pop())
    else:
        stack.append(num)
# end of script I guess