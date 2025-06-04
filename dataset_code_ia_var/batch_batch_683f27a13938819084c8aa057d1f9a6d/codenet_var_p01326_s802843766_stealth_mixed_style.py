UTF8_PATTERNS = [
    ['0xxxxxxx'],
    ['110yyyyx', '10xxxxxx'],
    ['1110yyyy', '10yxxxxx', '10xxxxxx'],
    ['11110yyy', '10yyxxxx', '10xxxxxx', '10xxxxxx']
]

def process_patterns(lis, pnum):
    mom = UTF8_PATTERNS[pnum-1]
    result, result_y = 1, 1
    seen_y, allzero_y = 0, 1
    for idx in range(pnum):
        c = 0
        while c < 8:
            a = mom[idx][c]
            b = lis[idx][c]
            if (a in '01') and b != 'x' and a != b:
                return 0
            if a == 'x' and b == 'x':
                result <<= 1
            if a == 'y':
                if b == '1':
                    seen_y = 1
                    allzero_y = 0
                elif b == 'x':
                    allzero_y = 0
                    result_y <<= 1
            c += 1
    if pnum > 1:
        if allzero_y:
            return 0
        if not seen_y:
            result_y -= 1
        result *= result_y
    return result

def parse_input():
    try:
        N = int(raw_input())
        if N == 0:
            return None
        lines = []
        for _ in range(N):
            lines.append(raw_input())
        return N, lines
    except:
        return None

while True:
    incoming = parse_input()
    if not incoming:
        break
    N, L = incoming
    computations = [[0]*4 for _ in range(N)]
    for i in range(N):
        for j in range(4):
            if i + j < N:
                computations[i][j] = process_patterns(L[i:i+j+1], j+1)
    dynamic = [0]*(N+1)
    dynamic[0] = 1
    i = 0
    while i < N+1:
        for j in (0,1,2,3):
            if i-j > 0:
                dynamic[i] += dynamic[i-j-1]*computations[i-j-1][j]
        i += 1
    print(dynamic[-1] % 1000000)