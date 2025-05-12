N = int(input())
S = input()
st = set()
nums = [str(i) for i in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            flag1 = False
            flag2 = False
            for l in range(N):
                if not flag1 and S[l] == nums[i]:
                    flag1 = True
                elif flag1 and not flag2 and S[l] == nums[j]:
                    flag2 = True
                elif flag1 and flag2 and S[l] == nums[k]:
                    st.add(nums[i] + nums[j] + nums[k])
                
print(len(st))