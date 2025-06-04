if __name__ == "__main__":
    # hmm, classic input method, but let's keep it for now.
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))  # not a, more explicit

    best = N + 1  # initialize with max possible + 1 (kind of big)
    j = 0
    count = 0
    freq = [0 for _ in range(K)]
    # Not a big fan of too many variables, but let's go
    for i in range(N):
        while j < N and count < K:
            x = arr[j]
            if x <= K:
                freq[x - 1] += 1
                if freq[x - 1] == 1:
                    count += 1
            j += 1

        if count == K:
            if j - i < best:
                best = j - i  # found better?

        x = arr[i]
        if x <= K:
            freq[x - 1] -= 1
            if freq[x - 1] == 0:
                count -= 1
        # reset step done, onto next iteration

    if best > N:
        print(0)
    else:
        print(best)
    # Hope this works, lol