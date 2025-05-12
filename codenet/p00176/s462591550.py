# 参考:http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2797666#1

COLOR = {
    "000000": "black",
    "0000ff": "blue",
    "00ff00": "lime",
    "00ffff": "aqua",
    "ff0000": "red",
    "ff00ff": "fuchsia",
    "ffff00": "yellow",
    "ffffff": "white"
}

while True:
    s = input()
    if len(s) == 1:
        break
    color = ""

    for first, second in zip(s[1::2], s[2::2]):
        if int(first + second, 16) <= 127:
            color += "00"
        else:
            color += "ff"
    print(COLOR[color])