n = int(input())
for _ in range(n):
    balls = list(map(int, input().split()))
    stack_b = []
    stack_c = []
    possible = True
    for ball in balls:
        can_b = not stack_b or stack_b[-1] > ball
        can_c = not stack_c or stack_c[-1] > ball
        if can_b and not can_c:
            stack_b.append(ball)
        elif can_c and not can_b:
            stack_c.append(ball)
        elif can_b and can_c:
            # Choisir la pile où l'on met la boule en faisant un choix réfléchi
            # pour éviter de bloquer plus tard.
            # On place sur la pile dont le sommet est le plus grand pour laisser plus
            # de chances à l'autre pile.
            if not stack_b:
                stack_b.append(ball)
            elif not stack_c:
                stack_c.append(ball)
            elif stack_b[-1] > stack_c[-1]:
                stack_b.append(ball)
            else:
                stack_c.append(ball)
        else:
            possible = False
            break
    print("YES" if possible else "NO")