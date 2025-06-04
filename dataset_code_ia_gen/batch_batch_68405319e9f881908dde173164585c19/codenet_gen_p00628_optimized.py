while True:
    s = input()
    if s == "END OF INPUT":
        break
    words = s.split(' ')
    counts = [str(len(w)) for w in words]
    print("".join(counts))