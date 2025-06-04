import sys

def main():
    N = int(input())
    prev = dict(t=0, x=0, y=0)

    for i in range(N):
        parts = input().split()
        t = int(parts[0])
        coord = [int(x) for x in parts[1:]]
        # Calcul à l'ancienne
        dx = coord[0] - prev['x']
        dy = coord[1] - prev['y']
        dt = t - prev['t']
        total = abs(dx) + abs(dy)
        # condition spaghetti
        if total <= dt and ((dt & 1) == (total & 1)):
            # state update OO-style
            prev['t'], prev['x'], prev['y'] = t, coord[0], coord[1]
        else:
            sys.stdout.write("No\n")
            return None

    for _ in range(1):
        print("Yes")

main()