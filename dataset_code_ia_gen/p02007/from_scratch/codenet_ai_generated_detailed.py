import sys
import bisect

def main():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]

    # Sort words lexicographically for prefix searching
    words.sort()
    # Create a reversed words list to efficiently find suffix matches by prefix searching on reversed words
    reversed_words = [''.join(reversed(w)) for w in words]
    reversed_words.sort()

    # For each query (prefix p, suffix s),
    # We'll find indices of words starting with p in words (normal lex order)
    # and indices of words ending with s in words (equivalent to words starting with reversed s in reversed_words)
    res = []
    for _ in range(Q):
        p, s = input().split()
        # prefix range in words
        p_start = p
        # make p_end string by incrementing last char to find upper bound prefix range
        # e.g. 'ab' -> 'ac'
        p_end = p[:-1] + chr(ord(p[-1]) + 1) if p else chr(ord('z')+1)
        # Find boundaries [left1, right1) for words starting with p
        left1 = bisect.bisect_left(words, p_start)
        right1 = bisect.bisect_left(words, p_end)

        # suffix search: words ending with s means reversed words starting with reversed(s)
        rs = s[::-1]
        rs_start = rs
        rs_end = rs[:-1] + chr(ord(rs[-1]) + 1) if rs else chr(ord('z')+1)
        left2 = bisect.bisect_left(reversed_words, rs_start)
        right2 = bisect.bisect_left(reversed_words, rs_end)

        # We have 2 ranges:
        # - words[left1:right1] start with prefix p
        # - reversed_words[left2:right2] start with rs (means words ending with s)
        # Need to count how many words are in intersection of these 2 sets.

        # The words array and reversed_words array correspond to same words in same order?
        # No, reversed_words is sorted on reversed strings, order differs.
        # We need a mapping from word -> index in words for efficiently checking intersection.

        # To handle large Q efficiently, prepare an id map: word -> id
        # And for reversed_words, prepare array of indexes in words sorted by reversed string.
        # Then for suffix range, we find the indexes in words array of the matching reversed_words,
        # and check how many are in [left1, right1) prefix range.

        # Let's build mapping word->id initially (outside loop)
        # and reversed_words ids list (outside loop)
        pass  # will implement after initial reading

    # To efficiently do the above intersection, we implement below after reading all words:
    # We proceed to implement the solution fully here, reorganizing to prepare data.

def solve():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)

    N, Q = map(int, input().split())
    words = [input().strip() for _ in range(N)]

    # words are unique, we sort them lex order and keep their original index
    words.sort()
    # Map word -> index in words
    word_to_index = {w: i for i, w in enumerate(words)}

    # reversed_words array: reversed strings of words list, we keep (reversed_word, original_index)
    reversed_words = []
    for i, w in enumerate(words):
        rw = w[::-1]
        reversed_words.append((rw, i))
    # sort by reversed_word
    reversed_words.sort(key=lambda x: x[0])

    # For quick binary search on reversed_words by reversed prefix (suffix), extract reversed_words keys into a separate array
    rev_keys = [rw for rw, _ in reversed_words]

    # For each query, we want:
    # 1. prefix range in words array: [left1, right1)
    # 2. suffix range in reversed_words array: [left2, right2)
    # Then count how many indices in reversed_words[left2:right2] lie in [left1, right1) of words indices

    # Because reversed_words contains original indices of words in increasing reversed_word order,
    # we get all indices that correspond to matching suffix,
    # we must check how many indices are within prefix range of words indices.

    # For efficient counting:
    # For each query:
    # - get list of indices of words with matching suffix (in reversed_words range)
    # - count how many of these indices in [left1, right1)

    # We'll do this using bisect on the list of indices (which is sorted as reversed_words are sorted by reversed_word)

    # Extract indices from reversed_words for each query suffix range, then count overlap with prefix range.

    for _ in range(Q):
        p, s = input().split()

        # prefix range in words
        p_start = p
        # Increment last char to get upper bound for prefix range
        # Handle case when p is empty (given problem states non-empty strings, so safe)
        p_end = p[:-1] + chr(ord(p[-1]) + 1)
        left1 = bisect.bisect_left(words, p_start)
        right1 = bisect.bisect_left(words, p_end)

        # suffix range in reversed_words
        rs = s[::-1]
        rs_start = rs
        rs_end = rs[:-1] + chr(ord(rs[-1]) + 1)
        left2 = bisect.bisect_left(rev_keys, rs_start)
        right2 = bisect.bisect_left(rev_keys, rs_end)

        # For candidates in reversed_words[left2:right2], we get their original indices
        candidate_indices = [idx for _, idx in reversed_words[left2:right2]]

        # candidate_indices are not guaranteed sorted, but in reversed_words they correspond to sorted reversed_word order,
        # the indices might be arbitrary. We sort them to enable bisect efficiently:
        candidate_indices.sort()

        # Count how many candidate_indices lie in [left1, right1)
        # Using bisect on candidate_indices
        left_pos = bisect.bisect_left(candidate_indices, left1)
        right_pos = bisect.bisect_left(candidate_indices, right1)
        print(right_pos - left_pos)

if __name__ == "__main__":
    solve()