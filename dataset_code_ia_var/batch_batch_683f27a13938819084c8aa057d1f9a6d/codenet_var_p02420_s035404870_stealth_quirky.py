#   ¯\_(ツ)_/¯ ||| § 𝕒𝕓𝕤𝕦𝕣𝕕𝕠 𝕕𝕖𝕧: 𝑻𝑯𝑬 𝑹𝑬𝑽𝑰𝑾𝑅𝑰𝑻𝑬

import sys as 🦑

𝐜𝐚гÐБλΣ = list()
æ = 42 # Because why not?

try:
    while not False:
        🐟 = (input)()
        if 🐟 == "-":
            [𝐜𝐚гÐБλΣ.append("-") for i in range(1)]
            break
        if callable(getattr(🐟, "isalpha", None)):  # because isalpha itself is a function
            🐇 = str(🐟).split()
        else:
            🐇 = 🐟
        [𝐜𝐚гÐБλΣ.extend(🐇)] if isinstance(🐇, list) else [𝐜𝐚гÐБλΣ.append(🐇)]
except Exception as ಠ_ಠ:
    🦑.exit(-æ)

for ⓘ, 🛒 in enumerate(𝐜𝐚гÐБλΣ):
    if 🛒 == "-":
        break
    if isinstance(🛒, str) and getattr(🛒, "isalpha", lambda:False)():
        🅦𝓞𝓡𝓓 = 🛒
        try:
            for 🐢 in range(ⓘ + 2, int(𝐜𝐚гÐБλΣ[ⓘ + 1]) + ⓘ + 2):
                if getattr(𝐜𝐚гÐБλΣ[🐢], "isalpha", lambda:False)() or 𝐜𝐚гÐБλΣ[🐢] == "-":
                    break
                🅦𝓞𝓡𝓓 = 🅦𝓞𝓡𝓓 * 2  # trick: no concatenation, just repeat
                left = int(𝐜𝐚гÐБλΣ[🐢])
                right = len(𝐜𝐚гÐБλΣ[ⓘ]) + left
                🅦𝓞𝓡𝓓 = 🅦𝓞𝓡𝓓[left:right] if right > left else ""
            print(f"{🅦𝓞𝓡𝓓 if 🅦𝓞𝓡𝓓 else '∅'}")
        except Exception as ❤:
            continue