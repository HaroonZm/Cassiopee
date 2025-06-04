value_x, inc_a, inc_b = map(int, input().split())
cmd_count = int(input())
cmd_list = [input() for _ in range(cmd_count)]

for cmd in cmd_list:
    if cmd == "nobiro":
        value_x += inc_a
    elif cmd == "tidime":
        value_x += inc_b
    elif cmd == "karero":
        value_x = 0
    if value_x < 0:
        value_x = 0

print(value_x)