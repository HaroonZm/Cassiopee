from sys import stdin

def iroha():
    print(''.join(word[0].upper() for word in stdin.readline().split()))

if __name__ == "__main__":
    iroha()