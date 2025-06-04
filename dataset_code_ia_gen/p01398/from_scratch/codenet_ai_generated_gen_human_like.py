def shift_char(c, diff):
    # -diff because we are reversing the encryption (which shifted backward)
    # but here we're decoding, so we shift forward by diff
    offset = (ord(c) - ord('a') + diff) % 26
    return chr(ord('a') + offset)

while True:
    N = input().strip()
    if N == '0':
        break
    N = int(N)
    message = list(input().strip())
    swaps = [tuple(map(int, input().split())) for _ in range(N)]

    # To decode, we must reverse the encryption steps in reverse order
    # because the encryption applied swaps from 1 to N
    # decoding applies swaps from N to 1 (inverse operation)
    for a, b in reversed(swaps):
        # indices to zero-based
        a -= 1
        b -= 1
        diff = abs(a - b)

        # first, reverse the character shifting:
        # encryption: took chars at a,b, swapped them,
        # then shifted both backward by diff.
        # So to decode:
        # before swapping back, shift both chars forward by diff
        message[a] = shift_char(message[a], diff)
        message[b] = shift_char(message[b], diff)

        # then swap back to original places
        message[a], message[b] = message[b], message[a]

    print("".join(message))