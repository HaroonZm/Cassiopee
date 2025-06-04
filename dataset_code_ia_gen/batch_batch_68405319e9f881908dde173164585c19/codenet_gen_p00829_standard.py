def main():
    import sys
    input = sys.stdin.read().strip().split()
    S = int(input[0])
    idx = 1
    MOD = 2**32
    for _ in range(S):
        data = list(map(lambda x: int(x,16), input[idx:idx+9]))
        idx += 9
        N = data[:8]
        chk = data[8]

        # sum of N modulo 2^32
        s = 0
        for v in N:
            s = (s + v) % MOD

        D = s ^ chk  # difference between sum and checksum

        key = 0
        for bit in range(32):
            bit_sum = 0
            for v in N:
                bit_sum ^= (v >> bit) & 1
            bit_chk = (chk >> bit) & 1
            # We want to find k_bit such that:
            # XOR over i=1..8 of (N_i^{bit} xor k_bit) == chk^{bit}
            # XOR over N_i^{bit} = bit_sum
            # So (bit_sum xor (k_bit if 8 is odd else 0)) = bit_chk
            # 8 is even, so effect is k_bit xor k_bit ... 8 times = 0 if even times, k_bit if odd times
            # Each bit of checksum is bit_sum xor (k_bit * (8 mod 2))
            # since 8 is even, this means k_bit * 0 = 0
            # So bit_chk == bit_sum if k_bit=0 => bit_chk == bit_sum if k_bit ==0
            # Or bit_chk == bit_sum xor 1 if k_bit=1 impossible since 8 is even
            # So if bit_sum != bit_chk then k_bit must flip bits in some way.
            # But problem says: the encryption is ni xor k
            # When XOR over N_i's xor with k:
            # XOR over N_i's xor with 8*k = XOR over N_i's xor 0 = XOR over N_i's
            # So sum xor checksum = D = k xor k xor ... 8 times is 0 (even times)
            # So the sum xor checksum = 0 if k=0
            # But we have difference D = sum xor checksum
            # Actually, the key is equal to D because:
            # XOR over all N_i's xor k 8 times: XOR over N xor (k xor k xor ...8 times) = XOR over N xor 0 = XOR N
            # So XOR N xor chk xor k = 0 => k = D
            # So k = D

        key = D
        print(hex(key)[2:] if key != 0 else '0')

if __name__ == "__main__":
    main()