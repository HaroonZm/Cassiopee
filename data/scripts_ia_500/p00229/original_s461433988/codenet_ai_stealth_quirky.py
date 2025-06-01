def main_loop():
    from sys import stdin as _stdin

    def _parse_line():
        return list(map(int, _stdin.readline().strip().split(" ")))

    _values = lambda: (_parse_line())

    while True:
        b, r, g, c, s, t = _values()
        if all(x == 0 for x in (b, r, g, c, s, t)):
            break
        # Expressions déplacées dans des variables non-signifiantes
        _calc1 = (b + r) * 15
        _calc2 = g * 7
        _calc3 = c * 2
        _calc4 = (b * 5 + r * 3) * 13
        _calc5 = (t - (s + b * 5 + r * 3)) * 3
        _result = 100 + _calc1 + _calc2 + _calc3 + _calc4 - _calc5
        print(_result)

main_loop()