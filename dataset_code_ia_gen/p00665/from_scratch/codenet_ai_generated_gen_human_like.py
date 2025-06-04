import sys
import bisect

input = sys.stdin.readline

while True:
    N, M, K, L = map(int, input().split())
    if N == M == K == L == 0:
        break

    chars = []
    name_to_votes = {}
    for _ in range(N):
        name, x = input().split()
        x = int(x)
        chars.append((name, x))
        name_to_votes[name] = x

    fav_names = [input().strip() for _ in range(M)]

    # Sort characters by (-votes, name) so higher votes first, ties by lex
    chars.sort(key=lambda c: (-c[1], c[0]))

    # Get the cut-off character for rank K (0-based index K-1)
    threshold_votes = None
    threshold_name = None
    if K <= N:
        threshold_votes = chars[K-1][1]
        threshold_name = chars[K-1][0]

    # Count how many chars have more votes than cut-off
    # These chars are definitely in top K
    more_votes_count = 0
    equal_votes_names = []
    for name, votes in chars:
        if votes > threshold_votes:
            more_votes_count += 1
        elif votes == threshold_votes:
            equal_votes_names.append(name)

    # The names at the threshold votes level sorted lex
    equal_votes_names.sort()

    # Number of spots available for chars equal to threshold votes
    spots_left = K - more_votes_count

    # Find index of threshold_name in equal_votes_names
    threshold_index = equal_votes_names.index(threshold_name)

    # The threshold group is equal_votes_names
    # The top spots_left of them can get in
    # The cut-off gets in if threshold_index < spots_left

    # We want to find how many favorites can get into top K
    # by distributing L votes.

    # Idea:
    # For a favorite f not currently in top K, need to surpass characters at rank K
    # i.e. need to get votes strictly greater than char currently at rank K

    # Determine for each favorite:
    # their current votes
    # how many votes needed to surpass the character at rank K

    # Let's create a helper list of votes to beat:
    # For the K-th rank character, need to strictly exceed their votes.
    # If place is shared (i.e equal votes), must beat the last lex char in threshold to get in.

    # Determine minimal votes needed to beat threshold
    # threshold_votes and threshold_name define last person in top K.

    # Conditions to be in top K:
    # - votes > threshold_votes, or
    # - votes == threshold_votes and name < threshold_name (lex order)

    # Let's implement comparison function:
    # To beat threshold:
    # - votes > threshold_votes or
    # - votes == threshold_votes and name < threshold_name

    # For each favorite, calculate minimal votes needed:
    # current_votes + delta > threshold_votes or
    # current_votes + delta == threshold_votes and favorite name < threshold_name

    # So minimal delta needed:
    # If current_votes > threshold_votes: zero (already above)
    # elif current_votes == threshold_votes:
    #   if name < threshold_name: zero
    #   else: need at least 1
    # else: threshold_votes - current_votes + 1

    fav_list = []
    for fname in fav_names:
        f_votes = name_to_votes[fname]
        # Determine minimal delta
        if f_votes > threshold_votes:
            needed = 0
        elif f_votes == threshold_votes:
            if fname < threshold_name:
                needed = 0
            else:
                needed = 1
        else:
            needed = threshold_votes - f_votes + 1
        fav_list.append((needed, fname, f_votes))

    # Sort favorites by needed votes ascending
    fav_list.sort()

    # Start with count of favorites already in top K (needed == 0)
    count = 0
    used_votes = 0

    # Spend votes on favorites in order of needed votes
    for needed, fname, f_votes in fav_list:
        if needed == 0:
            count += 1
        else:
            if used_votes + needed <= L:
                used_votes += needed
                count += 1
            else:
                break

    print(count)