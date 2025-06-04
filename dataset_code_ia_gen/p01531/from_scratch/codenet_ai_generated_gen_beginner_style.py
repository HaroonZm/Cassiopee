s = input()
button_map = {
    '1': 'a k s t n h m y r w'.split(),
    '2': 'a i u e o'.split(),
    '3': 'a k s t n h m y r w'.split(),
    '4': 'a k s t n h m y r w'.split(),
    '5': 'a k s t n h m y r w'.split(),
    '6': 'a k s t n h m y r w'.split(),
    '7': 'a k s t n h m y r w'.split(),
    '8': 'a k s t n h m y r w'.split(),
    '9': 'a k s t n h m y r w'.split(),
    '0': 'a i u e o'.split(),
}
# The above is not the right mapping, need to define the actual Japanese rows.

# As the problem is to output direct romaji strings for flick input with given mapping.
# Since the problem wants a beginner solution, do the mapping manually for each button and flick direction.

# Map for each button and flick direction to romaji
# Rows: a-gyou, ka-gyou, sa-gyou, ta-gyou, na-gyou, ha-gyou, ma-gyou, ya-gyou, ra-gyou, wa-gyou
# The buttons 1-9 and 0 correspond to each row as described.

# The mapping from button to row:
# '1': a-gyou (あ, い, う, え, お)
# '2': ka-gyou (か, き, く, け, こ)
# '3': sa-gyou (さ, し, す, せ, そ)
# '4': ta-gyou (た, ち, つ, て, と)
# '5': na-gyou (な, に, ぬ, ね, の)
# '6': ha-gyou (は, ひ, ふ, へ, ほ)
# '7': ma-gyou (ま, み, む, め, も)
# '8': ya-gyou (や, （い）, ゆ, （え）, よ) -- no い and え sounds, so only a, u, o
# '9': ra-gyou (ら, り, る, れ, ろ)
# '0': wa-gyou (わ, （い）, う, （え）, を, ん(only 0U))

# Mapping flick:
# T (touch): a-dan
# L (left): i-dan
# U (up): u-dan
# R (right): e-dan
# D (down): o-dan

# For ya-gyou and wa-gyou some vowels missing, so some flicks do not exist (and input never has invalid flicks)
# Also "ん" is produced by '0' flick up 'U'

# As the problem states, romaji consonants and vowels:
# a-gyou: a,i,u,e,o -> vowels only (a,i,u,e,o)
# ka-gyou: k + vowels
# sa-gyou: s + vowels (so, し is 'si' not 'shi')
# ta-gyou: t + vowels (ち is 'ti', つ is 'tu')
# na-gyou: n + vowels
# ha-gyou: h + vowels (ふ is 'hu')
# ma-gyou: m + vowels
# ya-gyou: y + vowels (only a,u,o)
# ra-gyou: r + vowels
# wa-gyou: w + vowels (only a,u,o), 'ん' is 'nn'

# Build a dictionary (button)(flick) -> romaji

romaji_map = {
    '1': {'T':'a', 'L':'i', 'U':'u', 'R':'e', 'D':'o'},
    '2': {'T':'ka', 'L':'ki', 'U':'ku', 'R':'ke', 'D':'ko'},
    '3': {'T':'sa', 'L':'si', 'U':'su', 'R':'se', 'D':'so'},
    '4': {'T':'ta', 'L':'ti', 'U':'tu', 'R':'te', 'D':'to'},
    '5': {'T':'na', 'L':'ni', 'U':'nu', 'R':'ne', 'D':'no'},
    '6': {'T':'ha', 'L':'hi', 'U':'hu', 'R':'he', 'D':'ho'},
    '7': {'T':'ma', 'L':'mi', 'U':'mu', 'R':'me', 'D':'mo'},
    '8': {'T':'ya', 'U':'yu', 'D':'yo'}, # no L or R flicks for ya-gyou
    '9': {'T':'ra', 'L':'ri', 'U':'ru', 'R':'re', 'D':'ro'},
    '0': {'T':'wa', 'U':'nn', 'D':'wo'}, # no L or R flicks for wa-gyou except 'nn' by up flick
}

res = ''
for i in range(0, len(s), 2):
    b = s[i]
    f = s[i+1]
    # Special check: for '8', only T, U, D allowed, so no L or R flicks will appear per problem statement
    # For '0', U flick outputs 'nn'
    romaji = romaji_map[b][f]
    res += romaji
print(res)