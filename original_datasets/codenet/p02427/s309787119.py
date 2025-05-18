if __name__ == "__main__":
    bit = int(input())

    print(f"0:")
    for d in range(1, 2 ** bit):
        print(f"{d}: ", end="")
        print(" ".join([str(elem) for elem in range(bit) if d & (1 << elem)]))