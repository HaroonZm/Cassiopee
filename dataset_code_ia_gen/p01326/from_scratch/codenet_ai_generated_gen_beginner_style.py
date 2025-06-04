def match_pattern(pattern, byte_str):
    for p, b in zip(pattern, byte_str):
        if p == '0' or p == '1':
            if b != p:
                return False
    return True

def count_possibilities(byte_str):
    # Count how many bytes possible for a single byte pattern matching byte_str
    # byte_str is 8 chars of '0','1','x'
    # returns number of possible bytes matching the pattern
    count = 0
    for i in range(256):
        b = format(i, '08b')
        match = True
        for ps, bs in zip(byte_str, b):
            if ps != 'x' and ps != bs:
                match = False
                break
        if match:
            count += 1
    return count

def count_valid_first_bytes(byte_str):
    # Count how many possible first bytes can be
    # and also return a list of the types (length) it can start
    # based on first byte bit pattern
    res = []
    for length in [1,2,3,4]:
        patterns = []
        if length == 1:
            # 0xxxxxxx
            # first bit 0
            pattern = '0xxxxxxx'
            if match_pattern(pattern, byte_str):
                # count possible bytes that fit pattern and byte_str
                cnt = count_possibilities(byte_str)
                if cnt > 0:
                    res.append((length, cnt))
        elif length == 2:
            # 110yyyyx 10xxxxxx
            # first byte pattern 110yyyyx with y having at least one 1 bit
            # Since only first byte here, just check first byte pattern
            # We'll check y bits later in extra check
            # 110yyyyx means bits: 1 1 0 y y y y x (bit0 is leftmost)
            # We'll check that y bits (bit3,4,5,6) are not all zero
            bits = list(byte_str)
            # check fixed bits
            if bits[0] in ['1','x'] and bits[1] in ['1','x'] and bits[2] in ['0','x']:
                ybits = bits[3:7]
                if 'x' in ybits:
                    # unclear y bits, count possibilities with y bits not all zero
                    count = 0
                    for i in range(256):
                        b = format(i,'08b')
                        ok = True
                        for pb, bb in zip(bits, b):
                            if pb != 'x' and pb != bb:
                                ok = False
                                break
                        if ok:
                            y = b[3:7]
                            # y bits must have at least one '1'
                            if '1' in y:
                                count += 1
                    if count > 0:
                        res.append((length, count))
                else:
                    # ybits known, check if at least one '1'
                    if '1' in ybits:
                        count = count_possibilities(byte_str)
                        if count > 0:
                            res.append((length, count))
        elif length == 3:
            # 1110yyyy 10yxxxxx 10xxxxxx
            # first byte pattern 1110yyyy and at least one y bit in first byte's y bits
            bits = list(byte_str)
            if bits[0] in ['1','x'] and bits[1] in ['1','x'] and bits[2] in ['1','x'] and bits[3] in ['0','x']:
                ybits = bits[4:8]
                if 'x' in ybits:
                    count = 0
                    for i in range(256):
                        b = format(i,'08b')
                        ok = True
                        for pb, bb in zip(bits, b):
                            if pb != 'x' and pb != bb:
                                ok = False
                                break
                        if ok:
                            y = b[4:8]
                            if '1' in y:
                                count += 1
                    if count > 0:
                        res.append((length, count))
                else:
                    if '1' in ybits:
                        count = count_possibilities(byte_str)
                        if count > 0:
                            res.append((length, count))
        elif length == 4:
            # 11110yyy 10yyxxxx 10xxxxxx 10xxxxxx
            # first byte pattern 11110yyy, y bits at positions 5,6,7 (0-based)
            bits = list(byte_str)
            if bits[0]=='1' or bits[0]=='x':
                if bits[1]=='1' or bits[1]=='x':
                    if bits[2]=='1' or bits[2]=='x':
                        if bits[3]=='1' or bits[3]=='x':
                            if bits[4]=='0' or bits[4]=='x':
                                ybits = bits[5:8]
                                if 'x' in ybits:
                                    count=0
                                    for i in range(256):
                                        b = format(i,'08b')
                                        ok = True
                                        for pb, bb in zip(bits, b):
                                            if pb != 'x' and pb != bb:
                                                ok = False
                                                break
                                        if ok:
                                            y = b[5:8]
                                            if '1' in y:
                                                count += 1
                                    if count > 0:
                                        res.append((length, count))
                                else:
                                    if '1' in ybits:
                                        count = count_possibilities(byte_str)
                                        if count > 0:
                                            res.append((length, count))
    return res

def count_following_byte(byte_str):
    # must match 10xxxxxx pattern
    # That means bits[0]='1', bits[1]='0', bits[2:] any
    bits = list(byte_str)
    if bits[0] not in ['1','x']:
        return 0
    if bits[1] not in ['0','x']:
        return 0
    # count possible matches
    count = 0
    for i in range(256):
        b = format(i,'08b')
        if b[0]!='1' or b[1]!='0':
            continue
        ok = True
        for pb, bb in zip(bits, b):
            if pb != 'x' and pb != bb:
                ok = False
                break
        if ok:
            count += 1
    return count

def main():
    MOD=1000000
    while True:
        N = int(input())
        if N == 0:
            break
        bytes_list = [input() for _ in range(N)]
        dp = [0]*(N+1)
        dp[0] = 1
        for i in range(N):
            if dp[i] == 0:
                continue
            # check first byte possibilities
            first_byte = bytes_list[i]
            start_bytes = count_valid_first_bytes(first_byte)
            for length, first_count in start_bytes:
                if i+length > N:
                    continue
                # check continuation bytes
                ok = True
                total = first_count
                for j in range(i+1, i+length):
                    cont_count = count_following_byte(bytes_list[j])
                    if cont_count == 0:
                        ok = False
                        break
                    total = (total * cont_count)%MOD
                if ok:
                    dp[i+length] = (dp[i+length] + dp[i]*total)%MOD
        print(dp[N]%MOD)
        
main()