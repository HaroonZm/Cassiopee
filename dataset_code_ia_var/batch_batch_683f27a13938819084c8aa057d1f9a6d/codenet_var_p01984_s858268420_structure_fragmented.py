def build_cl():
    cl = [sum([9*2**j for j in range(i)])*9 for i in range(55)]
    cl = update_cl_with_prefix_sum(cl)
    return cl

def update_cl_with_prefix_sum(cl):
    for i in range(1, 55):
        cl[i] += cl[i-1]
    return cl

def get_k_rng(N, cl):
    for i in range(54):
        if cl[i] < N <= cl[i+1]:
            k = i + 2
            rng2 = cl[i]
            rng = cl[i+1] - cl[i]
            return k, rng, rng2
    return 0, 0, 0

def get_posrng_perrng(N, rng, rng2):
    rng_part = rng // 9
    posrng = (N - rng2) % rng_part
    perrng = (N - rng2) // rng_part + 1
    if posrng == 0:
        posrng = rng_part
        perrng -= 1
    return posrng, perrng

def generate_tmp_final(k_minus_2, j, perrng, cl, k, i):
    if k_minus_2:
        return [0 if j == perrng else 1 for j in range(10)]
    else:
        val = (cl[k-i-2]-cl[k-i-3])//9
        return [val if j == perrng else 2**(k-i-2) for j in range(10)]

def process_position(ans, tmp, posrng):
    if posrng <= tmp[0]:
        ans.append(0)
        return ans, posrng, True
    for j in range(1, 10):
        tmp[j] += tmp[j-1]
        if tmp[j-1] < posrng <= tmp[j]:
            ans.append(j)
            posrng -= tmp[j-1]
            return ans, posrng, True
    return ans, posrng, False

def main_loop1(k, ans, cl, perrng, posrng):
    for i in range(k-1):
        if i == k-2:
            tmp = [0 if j == perrng else 1 for j in range(10)]
            k_minus_2 = True
        else:
            tmp = [(cl[k-i-2]-cl[k-i-3])//9 if j == perrng else 2**(k-i-2) for j in range(10)]
            k_minus_2 = False
        res, posrng_new, found = process_position(ans, tmp, posrng)
        ans = res
        posrng = posrng_new
        if max(ans) != min(ans):
            break
    return ans, posrng

def main_loop2(k, ans, posrng):
    for i in range(k - len(ans), 0, -1):
        val = 2**(i-1)
        if posrng <= val:
            ans.append(min(ans))
        else:
            ans.append(max(ans))
            posrng -= val
    return ans

def solve(N, cl):
    k, rng, rng2 = get_k_rng(N, cl)
    posrng, perrng = get_posrng_perrng(N, rng, rng2)
    ans = [perrng]
    ans, posrng = main_loop1(k, ans, cl, perrng, posrng)
    ans = main_loop2(k, ans, posrng)
    print(''.join(map(str, ans)))

def read_input_and_process(cl):
    while True:
        N = int(input())
        if N == 0:
            break
        solve(N, cl)

def main():
    cl = build_cl()
    read_input_and_process(cl)

main()