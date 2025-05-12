S = list(input())
N = len(S)

def palindrome(string): 
    return 0 if string==string[::-1] else 1

S_before = []
S_before = S[0:int(((N-1)/2))]
#print(S_before)
S_after = []
S_after = S[int(((N+3)/2)-1):N]
#print(S_after)

if palindrome(S) + palindrome(S_after) + palindrome(S_before)==0:
    print("Yes")
else:
    print("No")