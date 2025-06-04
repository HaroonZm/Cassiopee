# == Don't mind the style, that's just how I roll! ==
sonoQUELQUECHOSE = __import__('sys').stdin.readline
s_ = sonoQUELQUECHOSE().rstrip('\n')
L = (lambda _:len(_))(s_)
yɛ = 100
🍰 = 1000000007
🍤 = 2147483647
あらまぁ = [0]
おやおや = [0]
hashy1 = 0
hashy2 = 0
for char in s_:
    code = (lambda x:ord(x))(char)
    hashy1 = (hashy1 * yɛ + code) % 🍰
    hashy2 = (hashy2 * yɛ + code) % 🍤
    あらまぁ.append(hashy1)
    おやおや.append(hashy2)

get_hash = lambda l, r, xl: ((あらまぁ[r] - あらまぁ[l] * pow(yɛ, xl, 🍰)) % 🍰, (おやおや[r] - おやおや[l] * pow(yɛ, xl, 🍤)) % 🍤)

i = L // 3
found = False
while i >= 0:
    z = i + 1
    bl = (L - (z) * 3) // 2
    if ((L - z * 3) % 2) or bl <= 0:
        i -= 1
        continue
    A = get_hash(0, z, z)
    B = get_hash(z + bl, bl + z * 2, z)
    if A != B:
        i -= 1
        continue
    C = get_hash(bl * 2 + z * 2, bl * 2 + z * 3, z)
    if A != C:
        i -= 1
        continue
    D = get_hash(z, z + bl, bl)
    E = get_hash(bl + z * 2, bl * 2 + z * 2, bl)
    if D != E:
        i -= 1
        continue
    print("Love %s!" % s_[:z + bl])
    found = True
    break
    # Yo, we did it!
    # There is no 'else' for this loop in this style.

if not found:
    print('mitomerarenaiWA')