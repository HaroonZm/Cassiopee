import sys

MOD = 1000000

def count_matches(pattern, mask):
    # pattern & mask: arrays of bits or None for unknown
    # pattern bits: 0 or 1, mask bits: True if bit fixed, False if unknown
    # Count how many bits patterns conform to pattern/mask
    # For unknown bits 'x', they can be 0 or 1 -> 2 options each
    count = 1
    for i in range(8):
        if mask[i]:
            # fixed bit, only 1 option if bit matches
            pass
        else:
            # unknown bit: double options
            count = (count * 2) % MOD
    return count

def is_one_byte(b):
    # 0xxxxxxx: first bit = 0
    # b: list of chars '0','1','x'
    # first bit must be 0
    # bits 1..7 are any
    if b[0] == '1':
        return False
    if b[0] == 'x' or b[0] == '0':
        # fixed first bit is not 1, good
        return True
    return False

def count_one_byte(b):
    # first bit must be 0
    # bits after can be 0 or 1 or x
    # count possibilities that comply with first bit=0
    # So bit0 must be '0' or 'x' -> if 'x' then half possibilities have bit 0 = 0
    # But for 'x' first bit means 1 bit unknown -> bit0 = 0 or 1
    # Only accept bit0=0
    cnt=1
    # bit0
    if b[0] == '0':
        cnt=1
    elif b[0] == 'x':
        cnt=1  # only 1 possibility: zero, the other one is 1 and invalid => filter later
    else:
        return 0
    # bits 1..7: x or 0/1 any
    for i in range(1,8):
        if b[i] == 'x':
            cnt = (cnt*2)%MOD
    # For first bit 'x', only 1 of 2 possible bits (0 or 1) is valid (0).
    if b[0]=='x':
        cnt=cnt # since we counted only unknown bits after bit0
    return cnt

def count_two_byte(b1,b2):
    # two bytes:
    # 1st byte: 110yyyyx where y bits not all zero
    # bits in 1st byte:
    # 0:1,1:1,2:y,3:y,4:y,5:x
    # first byte bits:
    # bit0=1
    # bit1=1
    # bit2,3,4 = y bits, at least one 1
    # bit5 = x
    # bit6,7 can be anything?
    # Wait, pattern is 110yyyyx => bits: 1 1 0 y y y x
    # Actually per problem:
    # 2 bytes:
    # 110yyyyx 10xxxxxx
    # bits in first byte: b0=1, b1=1, b2=0, b3=y, b4=y, b5=y, b6=x
    # Actually: the problem says bits count from MSB (bit7) to bit0?
    # Standard UTF-8 (big endian bit order):
    # bits of a byte: b7 b6 b5 b4 b3 b2 b1 b0 (bit7 is MSB)
    # pattern 2-byte first byte:
    # 110yyyyx means:
    # bit7=1, bit6=1, bit5=0, bit4=y, bit3=y, bit2=y, bit1=x, bit0=?
    # but in problem: x can be any in x bits and y can be any 0/1 but not all zero.
    # From problem text pattern 2:
    # 110yyyyx 10xxxxxx
    # meaning:
    # byte1 bits: b7=1, b6=1, b5=0, b4=y, b3=y, b2=y, b1=x, b0=?
    # but 8 bit byte, so pattern exactly 8 bits:
    # 110yyyyx only has 8 bits
    # So b7=1,b6=1,b5=0,
    # b4=y1,b3=y2,b2=y3,b1=x,b0=x(??)
    # No, problem states:
    # For 2-byte char: 110yyyyx 10xxxxxx
    # meaning bits from left (MSB=bit7) to right(bit0):
    # first byte: bit7=1,6=1,5=0,4=y,3=y,2=y,1=x,0=x?
    # But problem only says y bits=3 bits, x bits= remaining bits.
    # Actually, from problem table:
    # 2-byte:
    # 110yyyyx 10xxxxxx  => byte1=bits: 1 1 0 y y y x x (bit7..bit0)
    # byte2=bits: 1 0 x x x x x x
    # So first byte bits: bit7=1, bit6=1, bit5=0, bit4=y, bit3=y, bit2=y, bit1=x, bit0=x
    # second byte bits: bit7=1, bit6=0, bits 5..0=x

    # y bits at positions: 4,3,2 in byte1
    # x bits at positions: 1,0 in byte1 and 5..0 in byte2
    # Must ensure at least one y bit=1

    # So parse b1 and b2 bits and check matching

    # Check fixed bits for first byte 110
    if b1[0] not in ('1','x'): # bit7 must be 1
        return 0
    if b1[1] not in ('1','x'): # bit6 must be 1
        return 0
    if b1[2] not in ('0','x'): # bit5 must be 0
        return 0

    # For second byte bits bit7=1, bit6=0 fixed
    if b2[0] not in ('1','x'): # bit7 must be 1
        return 0
    if b2[1] not in ('0','x'): # bit6 must be 0
        return 0

    # y bits at b1[3], b1[4], b1[5]
    y_bits_vals = []
    unknown_y = 0
    y_fixed_ones = 0
    for i in range(3,6):
        c = b1[i]
        if c == '1':
            y_fixed_ones +=1
            y_bits_vals.append(1)
        elif c == '0':
            y_bits_vals.append(0)
        else: # x
            y_bits_vals.append(-1)
            unknown_y +=1

    # must have at least one y bit=1
    # so count number of assignments to the unknown_y bits that produce at least one 1 with fixed ones included
    if y_fixed_ones > 0:
        y_valid_count = pow(2, unknown_y, MOD)
    else:
        # no fixed 1, so at least one unknown y bit must be 1
        # number of assignments for unknown_y bits = 2^unknown_y
        # excluding all zero assignment = 2^unknown_y -1
        if unknown_y ==0:
            # no unknown y bits, fixed ones=0, so no 1 possible -> invalid
            return 0
        y_valid_count = (pow(2, unknown_y, MOD) - 1) % MOD

    # For x bits in first byte: b1[6], b1[7]
    x1_count=1
    for i in range(6,8):
        if b1[i]=='x':
            x1_count = (x1_count*2)%MOD
        elif b1[i] in ('0','1'):
            pass
        else:
            return 0

    # For x bits in second byte: b2[2]..b2[7]
    x2_count=1
    for i in range(2,8):
        if b2[i]=='x':
            x2_count = (x2_count*2)%MOD
        elif b2[i] in ('0','1'):
            pass
        else:
            return 0

    total = (y_valid_count * x1_count) % MOD
    total = (total * x2_count) % MOD
    return total

def count_three_byte(b1,b2,b3):
    # 3 bytes:
    # 1110yyyy 10yxxxxx 10xxxxxx
    # byte1 bits: bit7=1,6=1,5=1,4=0,3=y,2=y,1=y,0=y
    # byte2 bits: 1 0 y x x x x x
    # byte3 bits: 1 0 x x x x x x
    # total y bits: 4 in byte1 + 1 in byte2 bit5= y bit
    # must have at least one y bit =1
    # Check fixed bits in byte1
    if b1[0] not in ('1','x'): # bit7=1
        return 0
    if b1[1] not in ('1','x'): # bit6=1
        return 0
    if b1[2] not in ('1','x'): # bit5=1
        return 0
    if b1[3] not in ('0','x'): # bit4=0
        return 0

    # Check fixed bits byte2
    if b2[0] not in ('1','x'): # bit7=1
        return 0
    if b2[1] not in ('0','x'): # bit6=0
        return 0

    # Check fixed bits byte3
    if b3[0] not in ('1','x'): # bit7=1
        return 0
    if b3[1] not in ('0','x'): # bit6=0
        return 0

    # y bits:
    # byte1 bits: bit3,2,1,0 (positions 3-0 in b1)
    # byte2 bit5 (position 5 in b2)
    y_positions_b1 = [3,2,1,0]
    y_positions_b2 = [2] #bit5 pos

    y_bits_list = []
    unknown_y = 0
    fixed_y_ones = 0
    # byte1 y bits
    for pos in y_positions_b1:
        c = b1[pos]
        if c == '1':
            fixed_y_ones +=1
            y_bits_list.append(1)
        elif c == '0':
            y_bits_list.append(0)
        else:
            y_bits_list.append(-1)
            unknown_y +=1
    # byte2 y bit
    c = b2[2]
    if c == '1':
        fixed_y_ones +=1
        y_bits_list.append(1)
    elif c == '0':
        y_bits_list.append(0)
    else:
        y_bits_list.append(-1)
        unknown_y +=1

    # check y bits constraint
    if fixed_y_ones > 0:
        y_valid_count = pow(2, unknown_y, MOD)
    else:
        if unknown_y == 0:
            return 0
        y_valid_count = (pow(2, unknown_y, MOD) - 1) % MOD

    # x bits count:
    # byte1 bits not checked: bit4 fixed (already 0), bits 5-7 fixed 1 1 1 already done
    # we accounted y bits and the others are fixed or y or x?

    # byte1 bits 5-7 fixed 111 done
    # byte1 bit4 fixed 0 done
    # bits 3,2,1,0 y bits handled

    # byte2 bits: bit7=1, bit6=0 done
    # bit5 y bit handled
    # bits 4,3,2,1,0 are x bits

    # byte3 bits: bit7=1, bit6=0 done
    # bits 5..0 x bits

    # count unknown x bits in byte1 (bits not y)
    # in byte1 bits are 8 bits:
    # bit7..bit0: [0],[1],[2],[3],[4],[5],[6],[7]
    # but careful: bits index 0 is MSB (bit7), index 7 is LSB (bit0) or is b1[0] bit7?
    # Actually b1[0] = bit7, b1[7] = bit0
    # So to understand bits numbering: b1[0]:bit7 (MSB), ... b1[7]: bit0 (LSB)
    # Previously we used bits as positions 0..7 = b1[0]..b1[7]

    # So byte1 bits:
    # bit7 : b1[0]
    # bit6 : b1[1]
    # bit5 : b1[2]
    # bit4 : b1[3]
    # bit3 : b1[4]
    # bit2 : b1[5]
    # bit1 : b1[6]
    # bit0 : b1[7]

    # Our previous y bits were b1[3],b1[4],b1[5],b1[6]?
    # Wait there is a mistake on y bits positions.

    # From initial problem analysis, 1110yyyy means byte1 bits:
    # bit7=1 b1[0]
    # bit6=1 b1[1]
    # bit5=1 b1[2]
    # bit4=0 b1[3]
    # bit3=y b1[4]
    # bit2=y b1[5]
    # bit1=y b1[6]
    # bit0=y b1[7]

    # So y bits in byte1 are b1[4],b1[5],b1[6],b1[7]

    # Similarly for byte2 10yxxxxx:
    # bit7=1 b2[0]
    # bit6=0 b2[1]
    # bit5=y b2[2]
    # bit4=x b2[3]
    # bit3=x b2[4]
    # bit2=x b2[5]
    # bit1=x b2[6]
    # bit0=x b2[7]

    # For byte3 10xxxxxx:
    # bit7=1 b3[0]
    # bit6=0 b3[1]
    # others x b3[2]-b3[7]

    y_bits_b1_idx = [4,5,6,7]
    y_bits_b2_idx = [2]

    y_bits_list = []
    unknown_y = 0
    fixed_y_ones = 0

    for idx in y_bits_b1_idx:
        c = b1[idx]
        if c == '1':
            fixed_y_ones +=1
            y_bits_list.append(1)
        elif c == '0':
            y_bits_list.append(0)
        elif c == 'x':
            y_bits_list.append(-1)
            unknown_y +=1
        else:
            return 0
    for idx in y_bits_b2_idx:
        c = b2[idx]
        if c == '1':
            fixed_y_ones +=1
            y_bits_list.append(1)
        elif c == '0':
            y_bits_list.append(0)
        elif c == 'x':
            y_bits_list.append(-1)
            unknown_y +=1
        else:
            return 0

    if fixed_y_ones > 0:
        y_valid_count = pow(2, unknown_y, MOD)
    else:
        if unknown_y == 0:
            return 0
        y_valid_count = (pow(2, unknown_y, MOD) -1) % MOD

    # Count x bits unknown
    # byte1 bits unknown x bits are bits not fixed and not y

    # byte1 bits: indexes 0..7
    # fixed bits:
    # b1[0-2]: fixed 1 1 1
    # b1[3]: fixed 0
    # b1[4-7]: y bits

    # So no x bits in byte1, all fixed or y bits.

    # byte2 bits:
    # b2[0]: fixed 1
    # b2[1]: fixed 0
    # b2[2]: y bit
    # b2[3]-b2[7]: x bits

    x_bits_b2_idx = [3,4,5,6,7]
    x2_count=1
    for idx in x_bits_b2_idx:
        c = b2[idx]
        if c == 'x':
            x2_count = (x2_count * 2) % MOD
        elif c in ('0','1'):
            pass
        else:
            return 0

    # byte3 bits:
    # b3[0] = 1 fixed
    # b3[1] = 0 fixed
    # b3[2..7] = x bits

    x_bits_b3_idx = [2,3,4,5,6,7]
    x3_count=1
    for idx in x_bits_b3_idx:
        c = b3[idx]
        if c == 'x':
            x3_count = (x3_count * 2) % MOD
        elif c in ('0','1'):
            pass
        else:
            return 0

    total = y_valid_count * x2_count % MOD
    total = (total * x3_count) % MOD
    return total

def count_four_byte(b1,b2,b3,b4):
    # 4 bytes:
    # 11110yyy 10yyxxxx 10xxxxxx 10xxxxxx
    # b1: 11110yyy: bit7=1,6=1,5=1,4=1,3=0,2=y,1=y,0=y
    # b2: 10yyxxxx: bit7=1,6=0