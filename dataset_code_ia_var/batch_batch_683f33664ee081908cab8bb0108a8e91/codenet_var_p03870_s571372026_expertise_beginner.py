import sys

def main():
    sys.setrecursionlimit(100010)
    n = int(sys.stdin.readline())
    nums = []
    for i in range(n):
        nums.append(int(sys.stdin.readline()))
    
    xor_all = 0
    for i in range(n):
        xor_all = xor_all ^ nums[i]
    
    # Convert xor_all to binary list
    bin_xor = bin(xor_all)[2:]
    bin_xor_list = []
    for i in range(len(bin_xor)):
        bin_xor_list.append(int(bin_xor[i]))
    
    # Make a delete list
    delete_list = []
    for i in range(len(bin_xor_list)):
        delete_list.append(0)
    
    for i in range(n):
        bin_num = bin(nums[i])[2:]
        bin_num = bin_num[::-1]  # reverse it so that [0] is the least significant bit
        for j in range(min(len(bin_num), len(bin_xor_list))):
            if bin_num[j] == '1':
                delete_list[j] = 1
                break
    
    delete_list = delete_list[::-1]
    
    ans = 0
    flip = 0
    for i in range(len(bin_xor_list)):
        bit = bin_xor_list[i]
        if bit ^ flip:
            if delete_list[i] == 1:
                flip = flip ^ 1
                ans = ans + 1
            else:
                print(-1)
                return
    
    if ans > n or n == 1:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()