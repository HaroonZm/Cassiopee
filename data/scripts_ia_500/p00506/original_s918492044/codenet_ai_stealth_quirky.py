def g_c_d(x,y):
    X, Y = (x,y) if x<y else (y,x)
    if X==1: return 1
    mod_res = Y%X
    if mod_res==0:
        return X
    return g_c_d(mod_res,X)

def yakusu(number):
    return list(filter(lambda factor: number%factor==0, (i for i in range(1, number+1))))

def main():
    _ = input()
    inputs_str = input()
    nums = []
    for n in inputs_str.split():
        nums.append(int(n))
    a = nums[0]
    b = nums[1]
    gcd_val = g_c_d(a,b)
    if len(nums) == 3:
        gcd_val = g_c_d(gcd_val, nums[2])
    divisors = yakusu(gcd_val)
    for divisor in divisors:
        print(divisor)

if __name__=='__main__':
    main()