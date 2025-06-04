A,B = map(int, input().split())
anna = list(map(int, input().split()))
bruno = list(map(int, input().split()))

# We want the longest common subarray between some subsequence of Anna's cards (any subset - but since order must be preserved, just any subsequence after removing 0 or more cards)
# and some contiguous subarray of Bruno's cards (since Bruno can only cut from the top or bottom, meaning a contiguous subarray).
# Because Anna can remove any cards from anywhere (not necessarily contiguous), her "subsequence" can skip cards arbitrarily.
# Bruno can only remove cards from the top and bottom, so the subarray he keeps is continuous.
# The score is the length of the matching sequence.

# The problem is to find the maximum length n of a sequence which appears as a subsequence in Anna's cards and a contiguous subarray in Bruno's cards.

# Approach:
# Since A and B can be up to 5000, it's feasible to use DP with O(A*B) complexity.
# We can use DP to find the longest common subarray ending at anna[i], bruno[j].
# For each pair (i,j), if anna[i]==bruno[j], dp[i][j] = dp[i-1][j-1] +1 else 0.
# This gives the length of longest common subarray ending at i,j.
# However, Anna's cards subsequence isn't necessarily contiguous but the DP above finds longest common contiguous suffix.
# But Anna can discard cards arbitrarily to make the resulting subsequence contiguous.

# Wait: The question states Anna can discard any cards she likes from anywhere to make her new pile. So the resulting pile in Anna's case must also be contiguous or any subsequence?
# Re-reading: "アンナはA枚のカードの中から任意の何枚か（0枚でもよい）を捨てて新しい山を作る." (Anna discards any cards at any positions and form a new pile)
# So Anna's new pile cards remain in the same relative order as original cards, but keep only a subsequence.
# Bruno only discards cards from top and bottom to form a contiguous subarray (the cards in the middle).
# The two piles must be exactly equal sequences.

# So the matching sequence must:
# - Appear as a subsequence in Anna's cards.
# - Appear as a contiguous subarray in Bruno's cards.

# To find the longest such sequence, we can consider all contiguous subarrays of Bruno's cards, and for each, check the length of its LCS with Anna's cards subsequence.

# But enumerating all B*(B+1)/2 subarrays will be O(B^2), which can be up to 25 million, borderline but might be too slow.

# Optimize:
# We'll reverse the roles.

# For each ending position j in Bruno's cards, we can create a DP to find the longest prefix suffix matching.

# Here's a better idea:
# For each position in Bruno, and length l, we consider the subarray bruno[j-l+1..j]

# Then, for all positions in Anna, we check if the subarray is subsequence of Anna's cards.

# Since Anna can remove cards arbitrarily but must keep order, subsequence matching is straightforward.

# So for speed, we fix the contiguous subarray in Bruno and check if it's subsequence of Anna.

# To check if a sequence is a subsequence of Anna efficiently:

# For Anna's cards, precompute positions of each number to speed up subsequence matching.

# But subsequence matching per query is O(A), so naive will be O(B^2 * A) = ~10^11 too big.

# Alternative approach:
# Let's switch the approach to find the longest common substring between Anna and Bruno with a twist:

# We want the longest common substring between Anna and Bruno.

# But Anna's subsequence must be contiguous because after discarding, their pile must be linear and contiguous.

# No, Anna can discard cards arbitrarily, so her pile is a subsequence, can be non-contiguous.

# So longest common substring won't work exactly.

# However, the matching sequence must be substring in Bruno and subsequence in Anna.

# So if we fix a substring of Bruno, we can check if it is a subsequence of Anna.

# Another way:

# Enumerate all substrings of Bruno from length L down to 1, check if substring is subsequence of Anna, and return max L for which yes.

# So binary search length L:

# For each length from max down to 1 (using binary search to reduce), we check all substrings of Bruno of length L.

# For each substring, check if it is subsequence of Anna.

# Since checking subsequence for length L substrings is O(A) per substring.

# For B=5000 and L ~2500, still expensive.

# Optimize subsequence checking:

# Preprocessing Anna:

# For Anna's cards, we can build next occurrence arrays for each card value:

# For each position i in Anna (0-based), next[i][v] = next occurrence of card v from position i.

# So to check subsequence of length L quickly:

# For substring s of Bruno, we can simulate traversing Anna's cards with next arrays:

# Start at pos = 0

# For each card c in substring s:

# pos = next[pos][c]

# If pos == -1 (no occurrence), fail

# else pos +=1 to move to next position

# If we reach the end successfully, substring s is subsequence.

# next arrays build:

# next[i][v] (i in 0..A) (A+1 size to handle end)

# For positions from A-1 downto 0:

# For each card value 1..1000, set next[i][v]:

# But storing next array for each position and each of 1000 cards is big:

# 5000*1000 = 5 million ints -- acceptable in memory.

# Build it.

# Then binary search length L from 0 to min(A, B)

# For each L, check all substrings of Bruno of length L if any is subsequence of Anna.

# If yes, set low=L+1

# else high=L

# Loop to find maximum.

# Implement.

INF = -1

max_card = 1000

# Build next array for Anna

next_pos = [[INF]*(max_card+1) for _ in range(A+1)]

for c in range(1,max_card+1):
    next_pos[A][c] = INF

for i in range(A-1,-1,-1):
    for c in range(1,max_card+1):
        next_pos[i][c] = next_pos[i+1][c]
    next_pos[i][anna[i]] = i

def is_subsequence(sub):
    pos =0
    for c in sub:
        pos = next_pos[pos][c]
        if pos == INF:
            return False
        pos +=1
    return True

low =0
high = min(A,B)+1

while low < high:
    mid = (low + high)//2
    found = False
    for start in range(B - mid + 1):
        sub = bruno[start:start+mid]
        if is_subsequence(sub):
            found = True
            break
    if found:
        low = mid +1
    else:
        high = mid

print(low-1)