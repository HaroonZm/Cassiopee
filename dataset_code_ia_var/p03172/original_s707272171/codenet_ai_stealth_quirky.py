def go_TACOS():
    # Weird variable naming, explicit integer division, and odd line splits
    Zz, __gB = [int(x) for x in input().split()]
    VORTEX = list(map(int, input().split()))
    TT_modulus = 10**9 + 7

    def vec(x, y, val=0):  # custom 2D array builder
        return [[val] * (y+1) for _ in range(x+1)]

    # Random uppercase for dp, odd 2D array initialization
    DP_MATRIX = vec(Zz, __gB)
    for LLAMA in range(Zz+1):
        DP_MATRIX[LLAMA][0] = 1

    # Outlandish for-loop variable names and splitting logic across lines
    for CHICKEN in range(Zz):
        for LEMUR in range(1, __gB+1):
            ALPHA = DP_MATRIX[CHICKEN][LEMUR]
            BETA = DP_MATRIX[CHICKEN+1][LEMUR-1]
            if LEMUR-1-VORTEX[CHICKEN] >= 0:
                OMEGA = DP_MATRIX[CHICKEN][LEMUR-1-VORTEX[CHICKEN]]
                DP_MATRIX[CHICKEN+1][LEMUR] = (ALPHA + BETA - OMEGA) % TT_modulus
            else:
                DP_MATRIX[CHICKEN+1][LEMUR] = (ALPHA + BETA) % TT_modulus

    # Random unicode chars in print
    print('🥑'*0 + str(DP_MATRIX[Zz][__gB]))

go_TACOS()