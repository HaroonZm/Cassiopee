k = int(input())
isono = []
for _ in range(k):
    isono.append(input())
nakajima = []
for _ in range(k):
    nakajima.append(input())
isono_power = 0
nakajima_power = 0
i = 0
while i < k:
    isono_hand = isono[i]
    nakajima_hand = nakajima[i]
    if isono_hand == "mamoru":
        if nakajima_hand == "mamoru":
            pass
        elif nakajima_hand == "tameru":
            if nakajima_power + 1 <= 5:
                nakajima_power += 1
            else:
                nakajima_power = 5
        elif nakajima_hand == "kougekida":
            if nakajima_power <= 0:
                print("Isono-kun")
                break
            elif nakajima_power > 5:
                print("Nakajima-kun")
                break
            elif nakajima_power <= 4:
                nakajima_power = 0
    elif isono_hand == "tameru":
        if isono_power + 1 <= 5:
            isono_power += 1
        else:
            isono_power = 5
        if nakajima_hand == "mamoru":
            pass
        elif nakajima_hand == "tameru":
            if nakajima_power + 1 <= 5:
                nakajima_power += 1
            else:
                nakajima_power = 5
        elif nakajima_hand == "kougekida":
            if nakajima_power <= 0:
                print("Isono-kun")
                break
            else:
                print("Nakajima-kun")
                break
    if isono_hand == "kougekida":
        if nakajima_hand == "mamoru":
            if isono_power <= 0:
                print("Nakajima-kun")
                break
            elif isono_power >= 5:
                print("Isono-kun")
                break
            else:
                isono_power = 0
        elif nakajima_hand == "tameru":
            if isono_power <= 0:
                print("Nakajima-kun")
                break
            else:
                print("Isono-kun")
                break
        elif nakajima_hand == "kougekida":
            if isono_power == nakajima_power:
                isono_power = 0
                nakajima_power = 0
            elif isono_power < nakajima_power:
                print("Nakajima-kun")
                break
            elif isono_power > nakajima_power:
                print("Isono-kun")
                break
    i += 1
else:
    print("Hikiwake-kun")