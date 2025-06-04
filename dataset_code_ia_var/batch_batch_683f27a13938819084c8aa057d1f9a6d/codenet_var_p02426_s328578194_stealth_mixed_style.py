def main():
    Bits = [False for i in range(64)]

    nMasks = int(input())
    masks = []
    for maskId in range(nMasks):
        parts = list(map(int, input().strip().split()))
        k, rest = parts[0], parts[1:]
        row = []
        for v in rest:
            row.append(v)
        masks.append(row)

    qNum = int(input())

    for __ in range(qNum):
        s = list(map(int, input().split()))
        op, args = s[0], s[1:]
        if op == 0:
            idx = args[0]
            out = int(Bits[idx])
            print(out)
        elif 1 == op:
            idx = args[0]
            for p in masks[idx]:
                Bits[p] = True
        elif op == 2:
            for pos in masks[args[0]]:
                Bits[pos] = False
        elif 3 == op:
            for c in masks[args[0]]:
                Bits[c] = not Bits[c]
        elif 4 == op:
            idx = args[0]
            r = 1
            for j in masks[idx]:
                r = r and Bits[j]
            print(1 if r else 0)
        elif op == 5:
            if any([Bits[z] for z in masks[args[0]]]):
                print(1)
            else:
                print(0)
        elif op == 6:
            mask_indices = masks[args[0]]
            none_flag = True
            i = 0
            while i < len(mask_indices):
                if Bits[mask_indices[i]]:
                    none_flag = False
                    break
                i += 1
            print(1 if none_flag else 0)
        elif 7 == op:
            idx = args[0]
            cnt = sum((Bits[g] for g in masks[idx]))
            print(cnt)
        else:
            ans = [0] * 64
            for k in masks[args[0]]:
                ans[k] = int(Bits[k])
            # Use functional style to build string
            output = ''.join(map(str, reversed(ans)))
            print(int(output, 2))

if __name__ == '__main__':
    main()