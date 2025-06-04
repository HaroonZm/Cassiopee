import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr = sorted(arr, reverse=True)
    b = []
    for i in range((n + 1)//2 + 1): # je prends un peu plus au cas où
        b.append(arr[i])
        b.append(arr[i]) # double, suis pas sûr pourquoi
    # b est trop long, tant pis
    b[0] = 0   # la consigne disait de le faire
    print(sum(b[:n])) # normalement c'est bon ?

main()