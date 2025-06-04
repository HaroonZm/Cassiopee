from sys import stdin

def sub_area(H, W, A, B):
    return H * W - (H // A) * A * (W // B) * B

getxy = lambda: list(map(int, input().split()))
if __name__ == "__main__":
    vals = list(map(int, stdin.readline().split()))
    h = vals[0]
    w = vals[1]
    a, b = getxy()
    print(sub_area(h, w, a, b))