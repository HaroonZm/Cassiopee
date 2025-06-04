n = int(input())
areas = []
for _ in range(n):
    areas.append(int(input()))

def is_possible(area):
    # 2xy + x + y = area
    # On cherche des x,y entiers positifs satisfaisant ça
    # On essaie x de 1 jusqu'à ce que 2x^2+x > area (borne raisonnable)
    for x in range(1, area+1):
        # Calcul de y possible
        # area = 2xy + x + y = y(2x+1) + x
        # y(2x+1) = area - x
        diff = area - x
        if diff <= 0:
            continue
        if diff % (2*x + 1) == 0:
            y = diff // (2*x + 1)
            if y > 0:
                return True
        if 2*x*x + x > area:
            break
    return False

count_wrong = 0
for area in areas:
    if not is_possible(area):
        count_wrong += 1

print(count_wrong)