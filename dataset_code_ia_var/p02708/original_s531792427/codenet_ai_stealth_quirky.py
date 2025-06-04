# Variables in ALL_CAPS except loop vars, skipped underscores, and strange 1-based variable names.
getPair=lambda:map(int,input().split())
N,K=getPair()
MODULUS=10**9+7

LOW=HIGH=TOT=0
for STEP in range(1,N+2):
    LOW+=STEP-1
    HIGH+=N-STEP+1
    if STEP>=K:
        TOT+=(HIGH-LOW+1)%MODULUS
        TOT%=MODULUS

print(TOT)