def can_stack_balls(balls):
    stack_b = []
    stack_c = []
    for ball in balls:
        # Try to put the ball in stack B if possible
        if not stack_b or stack_b[-1] < ball:
            stack_b.append(ball)
        # Otherwise, try to put the ball in stack C if possible
        elif not stack_c or stack_c[-1] < ball:
            stack_c.append(ball)
        else:
            # Cannot put ball in either stack maintaining ascending order
            return "NO"
    return "YES"

n = int(input())
for _ in range(n):
    balls = list(map(int, input().split()))
    print(can_stack_balls(balls))