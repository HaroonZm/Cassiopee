MAX = 10**9 * 2

while True:
    N = int(raw_input())
    if N == 0:
        break
    signal = raw_input().split(" ")
    min_x = MAX + 1
    max_x = - (MAX + 1)
    found_error = False
    for i in range(N):
        if signal[i] == "x":
            # Check for consecutive x's
            if i < N - 1 and signal[i + 1] == "x":
                print "none"
                found_error = True
                break
            # Odd position (1-based): restrict upper bound
            if (i + 1) % 2 != 0:
                if i <= 0:
                    left = MAX + 1
                else:
                    left = int(signal[i - 1])
                if i >= N - 1:
                    right = MAX + 1
                else:
                    right = int(signal[i + 1])
                if left < min_x:
                    min_x = left
                if right < min_x:
                    min_x = right
            # Even position: restrict lower bound
            else:
                if i <= 0:
                    left = - (MAX + 1)
                else:
                    left = int(signal[i - 1])
                if i >= N - 1:
                    right = - (MAX + 1)
                else:
                    right = int(signal[i + 1])
                if left > max_x:
                    max_x = left
                if right > max_x:
                    max_x = right
        else:
            # Check if the sequence alternates properly
            if i < N - 1 and signal[i + 1] != "x":
                cur = int(signal[i])
                nxt = int(signal[i + 1])
                if ( (i + 1) % 2 != 0 and cur >= nxt ) or ((i + 1) % 2 == 0 and cur <= nxt):
                    print "none"
                    found_error = True
                    break
    if found_error:
        continue
    answer = None
    temp_x = max_x + 1
    while temp_x < min_x:
        if answer is not None:
            print "ambiguous"
            break
        answer = temp_x
        temp_x += 1
    else:
        if answer is None:
            print "none"
        else:
            print answer