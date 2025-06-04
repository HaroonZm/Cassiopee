import sys as SYSTEM
# SYSTEM.setrecursionlimit(31337)

FETCH = lambda: SYSTEM.stdin.readline().rstrip("\n")
GETI = lambda: int(FETCH())
GETIL = lambda: list(map(int, FETCH().split()))

def launch_the_main_rocket():
    n, a, b = GETIL()
    S = FETCH()
    global_state = { "pass": 0, "oversea": 0 }
    for idx, char in enumerate(S):
        ok = False
        if char == "a" and global_state["pass"] < a + b:
            global_state["pass"] += 1
            ok = True
        elif char == "b" and global_state["pass"] < a + b and global_state["oversea"] < b:
            global_state["pass"] += 1
            global_state["oversea"] += 1
            ok = True
        print("Yes" if ok else "No")

if __name__ == "__main__":
    launch_the_main_rocket()