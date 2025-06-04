import sys

def main():
    input = sys.stdin.readline
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        w, v = map(int, input().split())
        if w != 0:
            ratio = v / w
        else:
            # Si w=0, on doit prendre x=1 si v>0, sinon x=0
            ratio = float('inf') if v > 0 else float('-inf')
        items.append((ratio, w, v))

    # Trier selon ratio décroissant
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    capacity = W

    for ratio, w, v in items:
        if w > 0:
            # Poids positif
            if capacity <= 0:
                break
            # On peut prendre au maximum un poids de capacity
            x = min(1, capacity / w)
            total_value += v * x
            capacity -= w * x
        elif w < 0:
            # Poids négatif
            # Prendre au max possible (x=1) augmente la capacité
            # On prend x=1 si ratio > 0
            if ratio <= 0:
                # ne pas prendre d'items avec poids negatif si ratio <=0 (pas rentable)
                continue
            # Prendre x=1
            total_value += v
            capacity -= w  # w<0 donc capacity augmente
        else:
            # w=0
            # Prendre x=1 si v>0, sinon x=0
            if v > 0:
                total_value += v

    print(f"{total_value:.6f}")

if __name__ == "__main__":
    main()