#!/usr/bin/env python3
import sys
sys.setrecursionlimit(50000)
def ryuka(n):
    dp = [0]*(n+1)
    
    def ryu(n):
        if n < 2:
            return 2 - n
        if dp[n] != 0:
            return dp[n]
        dp[n] = ryu(n-1)+ryu(n-2)
        return dp[n]

    return ryu(n)
print(ryuka(int(input())))