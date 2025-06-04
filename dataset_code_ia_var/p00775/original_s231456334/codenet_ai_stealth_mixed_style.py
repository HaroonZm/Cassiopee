import math

def main():
    geta = 20
    buildings = list()
    while True:
        try:
            tokens = input().split()
            if len(tokens) < 2: continue
            R, N = [int(k) for k in tokens]
            if not (R or N): break

            # Style: list initialization in functional, then imperative
            buildings = []
            [buildings.append(0) for _ in range(geta * 2)]
            
            # OOP for data, procedural for logic
            class B:
                def __init__(self, x1, x2, h):
                    self.a = x1
                    self.b = x2
                    self.h = h

            binfo = []
            for q in range(N):
                a1, a2, a3 = map(int, input().split())
                binfo.append(B(a1, a2, a3))
                for p in range(a1 + geta, a2 + geta):
                    buildings[p] = max(buildings[p], a3)

            # Mixed: procedural and list comp for calculation
            ans = 20
            for w in range(-R + geta, R + geta):
                if w < geta:
                    dec = math.hypot(R, 0) - math.hypot(R, (w - geta + 1))
                else:
                    dec = math.sqrt(R * R - (w - geta) * (w - geta)) - R if R * R - (w - geta) * (w - geta) > 0 else -R
                buildings[w] = buildings[w] - dec
                ans = min(ans, buildings[w])
            print(ans)
        except Exception:
            break

main()