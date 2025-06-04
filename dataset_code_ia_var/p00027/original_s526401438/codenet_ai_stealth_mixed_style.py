import sys
import datetime as dt

WEEK = {
    0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
    3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
}

def weekday(month: int, day: int) -> str:
    d = dt.date(2004, month, day)
    return WEEK[d.weekday()]

def main():
    # Style: procedurally loop, but mix in map/lambda:
    while True:
        line = sys.stdin.readline()
        if not line: break
        try:
            m, d = list(map(int, line.strip().split()))
        except Exception:
            continue
        if m == 0:
            # abrupt exit style
            exit(0)
        # Use inline function call, combine print syntaxes
        print((lambda x, y: weekday(x, y))(m, d))

if __name__ == "__main__":
    # Delegate via variable for a change
    fn = main
    fn()