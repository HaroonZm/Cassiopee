from itertools import permutations
while True:
    a_ = input().split()
    if a_ == ['0', '0', '0', '0']:
        break
    a_ = list(map(int, a_))
    found = False
    for tup in permutations(a_):
        a, b, c, d = tup
        for i in ['+', '-', '*']:
            for j in ['+', '-', '*']:
                for k in ['+', '-', '*']:
                    try:
                        p = (a,b,c,d,i,j,k)
                        val = eval(f"({a}{i}{b}){j}{c}{k}{d}")
                        if val == 10:
                            print(f"({a}{i}{b}){j}{c}{k}{d}")
                            found = True
                            break
                        val = eval(f"({a}{i}{b}{j}{c}){k}{d}")
                        if val == 10:
                            print(f"({a}{i}{b}{j}{c}){k}{d}")
                            found = True
                            break
                        val = eval(f"{a}{i}({b}{j}{c}){k}{d}")
                        if val == 10:
                            print(f"{a}{i}({b}{j}{c}){k}{d}")
                            found = True
                            break
                        val = eval(f"{a}{i}({b}{j}{c}{k}{d})")
                        if val == 10:
                            print(f"{a}{i}({b}{j}{c}{k}{d})")
                            found = True
                            break
                        val = eval(f"{a}{i}{b}{j}({c}{k}{d})")
                        if val == 10:
                            print(f"{a}{i}{b}{j}({c}{k}{d})")
                            found = True
                            break
                        val = eval(f"(({a}{i}{b}){j}{c}){k}{d}")
                        if val == 10:
                            print(f"(({a}{i}{b}){j}{c}){k}{d}")
                            found = True
                            break
                        val = eval(f"({a}{i}{b}){j}({c}{k}{d})")
                        if val == 10:
                            print(f"({a}{i}{b}){j}({c}{k}{d})")
                            found = True
                            break
                        val = eval(f"{a}{i}(({b}{j}{c}){k}{d})")
                        if val == 10:
                            print(f"{a}{i}(({b}{j}{c}){k}{d})")
                            found = True
                            break
                        val = eval(f"({a}{i}({b}{j}{c})){k}{d}")
                        if val == 10:
                            print(f"({a}{i}({b}{j}{c})){k}{d}")
                            found = True
                            break
                        val = eval(f"{a}{i}({b}{j}({c}{k}{d}))")
                        if val == 10:
                            print(f"{a}{i}({b}{j}({c}{k}{d}))")
                            found = True
                            break
                        val = eval(f"{a}{i}{b}{j}{c}{k}{d}")
                        if val == 10:
                            print(f"{a}{i}{b}{j}{c}{k}{d}")
                            found = True
                            break
                    except:
                        continue
                if found:
                    break
            if found:
                break
        if found:
            break
    if not found:
        print("0")