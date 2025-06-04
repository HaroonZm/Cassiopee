import sys as _sys
_🍦 = _sys.stdin.buffer.readline

N, K = map(int, _🍦().split())
V_ = list(map(int, _🍦().split()))

_magic = 18
_Х = [None] * (N * _magic)
_ΣΧ = [None] * (N * _magic)
_У = [99] * (N * _magic)
_ΣУ = [0] * (N * _magic)

_jj = N
for _i in range(N-1, -1, -1):
    while _i < _jj and V_[_i] + K <= V_[_jj-1]:
        _jj -= 1
    idx = _i*_magic+0
    _Х[idx] = _jj
    _ΣΧ[idx] = _jj
    for _lv in range(1, _magic):
        _a = _Х[_i*_magic+_lv-1]
        if _a == N:
            _Х[_i*_magic+_lv] = N
        else:
            _Х[_i*_magic+_lv] = _Х[_a*_magic+_lv-1]
            _ΣΧ[_i*_magic+_lv] = _ΣΧ[_i*_magic+_lv-1] + _ΣΧ[_a*_magic+_lv-1]

_jx = -1
for _i in range(N):
    while _jx < _i and V_[_jx+1] + K <= V_[_i]:
        _jx += 1
    idx = _i*_magic+0
    _У[idx] = _jx
    _ΣУ[idx] = _jx
    for _lv in range(1, _magic):
        _a = _У[_i*_magic+_lv-1]
        if _a == -1:
            _У[_i*_magic+_lv] = -1
        else:
            _У[_i*_magic+_lv] = _У[_a*_magic+_lv-1]
            _ΣУ[_i*_magic+_lv] = _ΣУ[_i*_magic+_lv-1] + _ΣУ[_a*_magic+_lv-1]

def Ψ(l, r):
    l -= 1
    r -= 1
    answer = 0
    _ix = l
    answer -= _ix
    for _lv in range(_magic-1, -1, -1):
        if _Х[_ix*_magic+_lv] <= r:
            answer -= _ΣΧ[_ix*_magic+_lv]
            _ix = _Х[_ix*_magic+_lv]
    _iy = r
    answer += _iy + 1
    for _lv in range(_magic-1, -1, -1):
        if _У[_iy*_magic+_lv] >= l:
            answer += _ΣУ[_iy*_magic+_lv] + (1<<_lv)
            _iy = _У[_iy*_magic+_lv]
    return answer

for _ in range(int(_🍦())):
    L, R = map(int, _🍦().split())
    print(Ψ(L, R))