max_val = 0
min_val = 1_000_000  # bien grand pour commencer

while True:
    try:
        val = float(input())
        if val > max_val:
            max_val = val  # hop, nouveau max
        elif val < min_val:
            min_val = val  # ça baisse ici
    except:
        diff = max_val - min_val
        print(f"{diff:.1f}")  # toujours un float avec 1 décimale
        break