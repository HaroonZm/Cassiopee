import sys

def main():
    q = int(input())
    my_dict = {}
    for i in range(q):
        parts = input().split()
        if parts[0] == '0':
            key = parts[1]
            value = int(parts[2])
            my_dict[key] = value
        else:
            key = parts[1]
            print(my_dict[key])

if __name__ == "__main__":
    main()