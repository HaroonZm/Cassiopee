import sys
import numpy as np
from functools import lru_cache

def offset(length):
    return 1 << length

def solve():
    n, k = map(int, sys.stdin.buffer.readline().split())
    buf = b"0" + sys.stdin.buffer.read().replace(b"\n", b"")
    table = np.frombuffer(buf, dtype=np.int8).astype(np.int32) - ord(b"0")

    # Precompute offset table efficiently
    offset_table = 1 << (np.arange(n + 1, dtype=np.int32) // 2)
    offset_table = offset_table[:len(table) // 2]

    ret = None

    for pos in range(n + 1):
        # Vectorized accumulation, advanced slicing
        slices = [slice(offset(length), offset(length + 1)) for length in range(pos + 1, n + 1)]
        for length, s in zip(range(pos + 1, n + 1), slices):
            width = 1 << pos
            # Summing the appropriate reshaped view over axis=0
            subtable = table[s]
            # Exploit stride tricks to avoid reshapes if possible
            table[offset(pos):offset(pos + 1)] += np.add.reduceat(subtable, np.arange(0, len(subtable), width))

        count_table = table[offset(pos):offset(pos + 1)]
        idx = np.flatnonzero(count_table >= k)
        if len(idx):
            ret = (idx[0], pos)
        else:
            return ret

        # Prepare transition tables with broadcasting
        for length in range(pos + 1, n + 1):
            size = 1 << length
            rest = length - pos
            half_period = 1 << (rest - 1)
            rng = np.arange(half_period + size, half_period + 2 * size, dtype=np.int32)
            trans_table = rng >> rest

            # Broadcasted arithmetic and np.roll for in-place updates
            factors = np.hstack((offset_table[:half_period], offset_table[half_period - 1::-1]))
            rolled = np.roll(np.arange(-half_period, half_period), half_period)
            trans_reshaped = trans_table.reshape(-1, half_period * 2)
            trans_reshaped *= factors
            trans_reshaped += rolled

            # Advanced in-place update
            np.add.at(table, trans_table, table[offset(length):offset(length + 1)])

    return ret

index, length = solve()
print(f'{index:020b}'[20-length:])