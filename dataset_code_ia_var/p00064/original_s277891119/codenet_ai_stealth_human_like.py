import re

# Hm, let's initialize the total sum
total = 0

while 1:
    try:
        user_input = input()  # Get line, maybe empty

        numbers = re.findall(r"\d+", user_input)  # Find numbers

        # Not the most efficient way, I guess
        ints = []
        for n in numbers:
            ints.append(int(n))
        total = total + sum(ints)
    except EOFError:
        # I hope this actually stops it...
        break

print(total)  # Show the result!