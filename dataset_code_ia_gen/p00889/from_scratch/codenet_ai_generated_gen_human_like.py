import sys
input = sys.stdin.readline

def main():
    while True:
        N,S,W,Q = map(int,input().split())
        if N == 0 and S == 0 and W == 0 and Q == 0:
            break

        g = S
        a = [0]*N
        for i in range(N):
            a[i] = (g//7) %10
            if g % 2 == 0:
                g = g//2
            else:
                g = (g//2) ^ W

        # We want to count pairs (i,j) with i<=j, a[i] != 0
        # and a_i...a_j as number % Q == 0.

        # Use prefix hashes modulo Q:
        # Let prefix_mod[k] = number represented by a[0..k-1] modulo Q
        # number a[i..j] mod Q = (prefix_mod[j+1] - prefix_mod[i]*pow10[j+1 - i]) mod Q

        prefix_mod = [0]*(N+1)
        pow10 = [1]*(N+1)
        for i in range(N):
            prefix_mod[i+1] = (prefix_mod[i]*10 + a[i]) % Q
            pow10[i+1] = (pow10[i]*10) % Q

        count = 0
        freq = dict()
        # We will iterate i from 0 to N-1 as start index of substring
        # But only those i with a[i]!=0 count as valid start

        # Instead of iterating j for each i, we can fix end j and count prefixes

        # We can process from left to right:
        # At each position j, prefix_mod[j+1] corresponds to number a[0..j]
        # For substring a[i..j]:
        # number mod Q = (prefix_mod[j+1] - prefix_mod[i]*pow10[j+1 - i]) mod Q == 0
        # => prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i] mod Q

        # Since starting zeros are invalid, only consider i where a[i]!=0

        # Approach:
        # For each j, check all i <= j where a[i]!=0 and prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i] mod Q
        # This is expensive O(N^2).
        # Alternative approach:

        # Fix end j and for all prefix_mod[i], i<=j+1, a[i]!=0, 
        # try to find how many i satisfy prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i] mod Q

        # We can't do this directly.

        # Instead, iterate i from N-1 down to 0:

        # For substrings starting at i (with a[i]!=0), we can process substrings a[i..j] for j>=i.

        # To optimize, we use a map freq that stores count of prefix_mod values for substrings starting at positions.

        # Alternatively, we process from left:
        # For all substrings ending at j:

        # Let's precompute:
        # For each position i where a[i]!=0, store (prefix_mod[i], i) in a map to count frequencies.

        # Then for each j, we want count of i <= j with a[i]!=0 and prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i] mod Q.

        # Let x = prefix_mod[i]
        # We want prefix_mod[j+1] == x * pow10[j+1 - i] mod Q
        # => x == prefix_mod[j+1] * pow10_inv[j+1 - i] mod Q, where pow10_inv is modular inverse of pow10.

        # Since Q is prime, we can use Fermat's little theorem for inverse modulo.

        # Precompute pow10_inv:

        def modinv(x,m):
            # Fermat's little theorem, since Q is prime
            return pow(x,m-2,m)
        pow10_inv = [1]*(N+1)
        inv_10 = modinv(10,Q)
        for i in range(1,N+1):
            pow10_inv[i] = (pow10_inv[i-1]*inv_10)%Q

        # For each position i with a[i]!=0, store prefix_mod[i] in freq map keyed by index i
        # But searching i for each j is too slow

        # We can invert the approach:
        # For each j, compute prefix_mod[j+1]
        # For each length L=1..j+1:
        # i = j+1 - L
        # if a[i]!=0:
        # x = prefix_mod[i]
        # Check if prefix_mod[j+1] == x * pow10[L] mod Q

        # Still O(N^2) too slow.

        # Better approach:

        # We'll process substrings in order of increasing length:
        # But need an O(N) or O(N log N) method.

        # Proposed efficient solution:
        # We iterate the sequence once from left to right, maintaining a map freq which maps from prefix_mod values to counts of positions i with a[i]!=0 and prefix_mod[i]

        # At position j+1, we want to find number of i's where:
        # prefix_mod[j+1] == prefix_mod[i] * pow10[j+1 - i] mod Q, and a[i]!=0

        # Rearranged:
        # prefix_mod[i] == prefix_mod[j+1] * pow10_inv[j+1 - i] mod Q

        # So for each j, we try to find count of i in freq with prefix_mod[i] == val for val = prefix_mod[j+1]*pow10_inv[len] mod Q where len = j+1 - i

        # We cannot try all i's for j, but we can invert indexing:

        # For each j, we try all possible len? No.

        # Alternative plan: fix i, and sum over j.

        # Actually, better plan:

        # For each position i with a[i]!=0, consider all ends j >= i.

        # For substring a[i..j]:
        # number mod Q = (prefix_mod[j+1] - prefix_mod[i]*pow10[j+1 - i]) mod Q == 0
        # => prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i] mod Q

        # For fixed i, the values prefix_mod[i]*pow10[len] mod Q for len=1...N-i, for each j=i+len-1,is the required prefix_mod[j+1].

        # So if we build a map from prefix_mod values to list of positions, we can for each i count how many j+1 positions have prefix_mod[j+1]== prefix_mod[i]*pow10[len]

        # Idea: Build inverse map from prefix_mod values to counts per position.

        # To make this efficient, process prefix_mod from left to right, count frequencies of prefix_mod.

        # We can store count of prefix_mod occurrences in freq_global.

        # Then for each i with a[i]!=0, and for lengths from 1 upto...? Can't do all lengths.

        # To do it in O(N):

        # Let's reverse the problem:

        # For any substring that is multiple of Q, prefix_mod[j+1] == prefix_mod[i]*pow10[j+1 - i]

        # Or prefix_mod[j+1] * pow10_inv[j+1 - i] == prefix_mod[i]

        # If we fix the substring end j, then for len = 1..j+1, i = j+1 - len

        # For each j+1, we want to find number of i with a[i]!=0 and prefix_mod[i] == prefix_mod[j+1]*pow10_inv[len]

        # We can prepare a data structure that, for each prefix_mod value stores sorted positions i where a[i]!=0.

        # Then for each j, do binary search to count how many i <=j with prefix_mod[i] == needed value.

        # Since N can be 10^5, this approach is possible.

        # Implement:

        from collections import defaultdict
        pos_map = defaultdict(list)
        for i in range(N+1):
            # a[i] is defined for i in [0..N-1] only
            # prefix_mod has length N+1
            # We want to collect positions i with a[i]!=0, but prefix_mod is indexed at i
            if i < N and a[i] != 0:
                pos_map[prefix_mod[i]].append(i)

        # For each j from 0 to N-1, substring ends at j, prefix_mod index j+1

        # For all lengths l=1..j+1:
        # i = j+1 - l

        # We want count of i where prefix_mod[i] == val = prefix_mod[j+1]*pow10_inv[l] mod Q, i <= j, a[i]!=0

        # Enumerating all lengths l is O(N^2) too large.

        # Need further optimization:

        # For each prefix_mod value, the positions are sorted.

        # For each prefix_mod[j+1], we can try all pow10_inv[l], but again too large.

        # So alternative is to swap loops:

        # For each prefix_mod value x in pos_map:

        # For each position i in pos_map[x]:

        # For j>=i, want prefix_mod[j+1] == x * pow10[j+1 - i]

        # So for j+1 in [i+1..N], value v = x * pow10[j+1 - i] mod Q

        # For fixed x and i, generate the required prefix_mod values for j+1 from i+1 to N.

        # For all j+1 - i = length from 1 to N - i

        # So for each length l=1 to N - i:

        # v = x * pow10[l] mod Q

        # For each v, check how many prefix_mod[] equals v at positions j+1 >= i+1

        # We can build an index mapping from prefix_mod values to positions (prefix_mod indices).

        # Then use binary search to count number of prefix_mod indices >= i+1 with value v.

        # Implement this:

        # Build pos_prefix_mod: map prefix_mod value -> sorted list of positions (from [0..N])

        val_pos = defaultdict(list)
        for idx,v in enumerate(prefix_mod):
            val_pos[v].append(idx)

        import bisect
        ans = 0
        for x, positions in pos_map.items():
            # positions sorted ascending
            for i in positions:
                max_len = N - i  # substring length max
                for length in range(1, max_len+1):
                    v = (x * pow10[length]) % Q
                    arr = val_pos.get(v,[])
                    if not arr:
                        continue
                    # Need count of positions j+1 >= i+1 in arr
                    idx = bisect.bisect_left(arr, i+1)
                    count_here = len(arr) - idx
                    ans += count_here
                    # To speed up, break early if count_here==0
                    if count_here == 0:
                        # no further larger j exists for this v
                        pass
                # This loop is O(N) per i worst case, total O(N^2), too slow

        # The above is too slow for large data.

        # We need a better approach.

        # Final optimized approach:

        # Since leading zeros are forbidden, substrings start only at positions i where a[i]!=0.

        # Instead of checking all substrings, we iterate over the sequence.

        # Define:

        # rem = 0
        # For j in [0..N-1]:
        #   Update rem = (rem*10 + a[j])%Q

        # We keep a map cnt[count of prefix_mod value with starting positions]
        # For substrings starting at positions i where a[i]!=0

        # We process from left to right:

        # Initialize result = 0
        # freq map from prefix_mod values to count
        # We can only count substrings with leading digit non-zero,
        # so when a[j]!=0, we start new counts.

        # Actually, solution given in editorial uses the property that Q is prime.

        # The problem can be solved using hashing + prefix counts + walking once.

        # Implementation from scratch:

        freq = defaultdict(int)
        freq[0] = 1 # empty prefix count

        ans = 0
        rem = 0
        start = 0
        for i in range(N):
            if a[i] == 0:
                # cannot start substring here
                rem = 0
                freq = defaultdict(int)
                freq[0] =1
                start = i+1
                continue
            rem = (rem*10 + a[i])%Q
            # Count how many previous prefix_mod == rem to have substring divisible by Q
            ans += freq[rem]
            freq[rem] +=1

        print(ans)

if __name__ == "__main__":
    main()