def solve(h,w):
    ans1 = float("inf")
    ans2 = float("inf")
    for i in range(1,h):
        w_mid = w//2
        s1_max = max(i*w,(h-i)*w_mid,(h-i)*(w-w_mid))
        s1_min = min(i*w,(h-i)*w_mid,(h-i)*(w-w_mid))
        ans1 = min(ans1,s1_max - s1_min)
    for i in range(1,h):
        h_mid = (h-i)//2
        s2_max = max(i*w,h_mid*w,(h-i-h_mid)*w)
        s2_min = min(i*w,h_mid*w,(h-i-h_mid)*w)
        ans2 = min(ans2,s2_max-s2_min)
    return min(ans1,ans2)
def main():
    h,w = map(int,input().split())
    print(min(solve(h,w),solve(w,h)))
if __name__=='__main__':
    main()