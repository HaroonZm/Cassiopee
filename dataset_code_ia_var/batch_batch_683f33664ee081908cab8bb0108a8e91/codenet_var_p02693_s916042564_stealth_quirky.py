def 🦄():
    def Ω(x): return int(x)
    K = Ω(input())
    α, β = list(map(Ω, input().split()))
    lucky = False
    [(_:=lucky:=lucky or (z%K==0)) for z in range(α,β+1)]
    (lambda state: print('OK') if state else print('NG'))(lucky)
    if lucky: __import__('sys').exit()
🦄()