import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7
MAX_Q = 10**6

def main():
    input = sys.stdin.readline

    N = int(input())
    q = list(map(int, input().split()))

    # Step 1: Precompute the smallest prime factor (spf) for each number up to MAX_Q
    # This allows us to quickly check prime status and factorize numbers up to 10^6
    spf = [0] * (MAX_Q + 1)
    spf[1] = 1
    for i in range(2, MAX_Q +1):
        spf[i] = 0

    for i in range(2, int(MAX_Q**0.5) + 1):
        if spf[i] == 0: 
            for j in range(i*i, MAX_Q+1, i):
                if spf[j] == 0:
                    spf[j] = i
    # After this, for primes spf[x] == 0, for composite smallest prime factor is stored.

    # Step 2: Analyze q to identify prime bases (p_i) and exponents (e_i)
    # According to the problem:
    # - If e_i == 1, q[i] = p_i (prime)
    # - If e_i > 1, q[i] = p_i^e_i (power), with p_i prime and e_i>1
    # We must:
    # - Parse q[i]
    # - Confirm that p_i is prime
    # - Confirm q[i] = p_i^e_i exactly
    # - Map consecutive q[i] with same p_i to the same factor, this comes from the problem examples.
    #
    # Actually the display merges the factorization but with a twist:
    # If exponent is 1, display pi once.
    # If exponent >1, display pi and then exponent ei separately.
    #
    # So the sequence q is a sequence of tokens representing prime factors and exponents.
    #
    # We must reconstruct the factorization from q:
    # factors are sorted ascending by prime p_i
    # The display shows p_i (if exponent is 1), or p_i e_i (two elements)
    #
    # So we scan q left to right:
    # - if q[i] is prime, it is either p_i with e_i=1 or the base of exponent >1 factor
    # - if next q[i+1] is prime, then it's the next prime factor with e_i=1
    # - if next q[i+1] is NOT prime, then q[i+1] is exponent e_i for prime p_i = q[i]

    # However q can contain numbers > 10^6? No, from constraints q_i <= 10^6.

    # To recall from samples:
    # For input: 2 3 3
    # Output: 2 numbers: 24=2^3*3^1 and 54=2^1*3^3
    # So for q=[2,3,3], we find "2 3" and "3" => p1=2, e1=1 or e1=3, p2=3, e2=3 or 1
    # This means that the machine output is "display" tokens, and we have to count how many factorization match the display sequence, allowing exponents to be swapped between bases of the same prime numbers appearing twice

    # The problem is equivalent to:
    # Given a sequence q (length N), count how many factorizations M with distinct primes p_i in ascending order exist,
    # such that the display output matches q exactly (the display output format is explained).

    # On close reading of the problem and samples:
    # The output q corresponds exactly to the machine display output.
    # The display is constructed from the factorization p1^e1 * p2^e2 * ... * pK^eK by:
    # For each prime factor:
    #  - if e_i=1, output p_i
    #  - else output p_i and e_i separated (two tokens)
    # In order of ascending p_i.

    # So the q sequence is a tokenized factorization display, but concatenated for multiple factors in ascending order.

    # For the sample input1 q=[2,3,3] the display corresponds to:
    # 2 3 3
    # That can be parsed as either:
    # - 2 3 3 which could mean prime factor 2 with exponent 3 (tokens: 2 3), and prime factor 3 with exponent 1 (token: 3)
    # - OR prime factor 2 with exponent 1 (token: 2), prime factor 3 with exponent 3 (tokens: 3 3)
    # So the display can correspond to multiple factorizations depending on how to parse q
    # Thus we must count number of valid parses of q into factor-exponent pairs (where exponent can be omitted if 1)
    # AND exponent must be integer >=1 (and the exponent token must be prime > 1)
    # Exponent must be an integer, but the problem constraints say q_i >= 2, so exponent >=2 is possible.

    # Step 3: Implement DP to count number of parses of q satisfying:
    # At position i:
    # - if q[i] is prime => we can parse factor with exponent=1 [consume 1 token]
    # - or if q[i] is prime and i+1 < N and q[i+1] is prime (can't be an exponent if prime?)
    #   Exponent token can be any integer >=2, but must correspond to prime factorization with prime base
    #   Actually the problem states:
    #    If e_i=1, display p_i (prime).
    #    else display p_i e_i (e_i is exponent integer>=2, output as decimal digits, but machine shows only digits and whitespace)
    #
    # But in q, all tokens are integers >=2 up to 10^6.
    #
    # In particular, the exponent token is a positive integer >= 2.
    #
    # We must check if the exponent token is a positive integer: yes, from input.
    #
    # Also exponent token correspond to the exponent count e_i (>=2 integer).
    #
    # Thus for parsing:
    # at i, if q[i] is prime (check), then:
    #    option1: factor with exponent 1, move i+1
    #    option2: if i+1 < N and q[i+1] is integer exponent >=2, parse factor p_i=q[i] with e_i=q[i+1], move i+2
    #
    # BUT exponent can be any integer >= 2 (not necessarily prime), e.g. sample input 2 has exponent 4 which is not prime.
    # So the exponent token can be composite integer, no prime check on exponent token.
    #
    # So exponent token can be any q[i+1]>=2 (always true)
    # So just accept it as exponent.

    # Step 4: Important check:
    # primes p_i are strictly ascending in the factorization.
    # So the primes extracted in the parsing must be in ascending order.
    #
    # So when parsing next factor, p_i must be strictly greater than previous prime p_i

    # However, q can contain tokens not representing primes:
    # if at position i token q[i] is not prime => invalid parse => 0 count

    # So in DP, keep track of dp[i] = number of valid parses of q[i:]
    # with variable last_prime to store last prime factor chosen to verify ascending order

    # to prevent complexity, do not store last_prime in dp keys as it is too big,
    # but primes are up to 10^6.

    # Hence we can make a dp with memory optimization:
    # since prime has to be strictly ascending:
    # - We'll process from left to right
    # - At each position i, candidate prime q[i] must be > last_prime

    # To apply last_prime restriction, we must store dp by position and last_prime

    # last_prime ranges up to 10^6, too large for dp.

    # But from problem constraints and pattern, can we process by greedy way?

    # The input q is the concatenation of terms:
    # For each prime factor p_i, display equals [p_i] if exponent==1, else [p_i, e_i]

    # So the factorization we try to reconstruct is unique with respect to p_i.

    # The problem is that some primes can appear repeatedly, because q can have repeated primes, as in sample input 1 q=[2,3,3]

    # Because ordering of primes in p_i is ascending, and the display is sorted accordingly, we must assign prime factors accordingly

    # But in sample input 1, two '3's appear consecutively: 2 3 3
    # That corresponds to two possible factorizations:
    # (2^3)*(3^1) or (2^1)*(3^3)

    # So the factorization isn't unique, but the question is how many numbers produce the displayed q.

    # So the problem reduces to counting the number of ways to parse q into prime factor-exponent sequences where the primes are strictly increasing.

    # The challenge is the last_prime restriction, and ambiguous exponent parsing.

    # Let's consider that at position i, we do not store last_prime in dp but we try to use the ascending order of q[i]:

    # Since primes must be strictly ascending, and q is composed of primes and exponents.

    # We can pre-check that q is sorted ascending with exponents included or not?

    # From problem description: output tokens are displayed in ascending order by prime factor p_i, with a special format for exponent.

    # Hence the display tokens are as follows:

    # For factor p_i with exponent e_i:
    # display tokens:
    #   p_i
    #   e_i (only if e_i > 1)
    #
    # The list q is concatenation of all factor display tokens

    # Therefore the q tokens are sorted by the prime p_i ascending:
    #
    # Each prime factor's display tokens are either length 1 (if e_i=1) or length 2 (if e_i>1)

    # The problem reduces to segmenting q into consecutive "factor displays" each of length 1 or 2,
    # where the first token in each factor display is prime
    # the exponent token (when length 2) is a positive integer >= 2 (can be composite)
    #
    # And the primes in the factor displays must be strictly ascending.

    # So let's parse q left to right, try all decompositions:

    # The dp is dp[i] = number of ways to segment q[i:] into correct factor displays with primes strictly ascending, given last_prime assigned before i.

    # The only complication is the last_prime checking: to implement dp easily, we store last_prime in dp state.

    # last_prime can be 0 at start (because no prime yet)

    # There are up to 10^5 tokens, and last_prime can be 0..10^6.

    # dp dimension too large for (i, last_prime), but last_prime is always increasing in state transitions.

    # Since last_prime always increases, number of states with dp[i][last_prime] is manageable if we memoize.

    # Let's implement dp with recursion and memoization.

    from functools import lru_cache

    # Check primality fast with spf: spf[x] ==0 => prime, else composite.
    def is_prime(x):
        if x <= 1:
            return False
        return spf[x] == 0

    @lru_cache(maxsize=None)
    def dfs(i, last_prime):
        # Return number of ways to parse q[i:] where primes chosen strictly > last_prime
        if i == N:
            return 1

        res = 0

        # Case 1: Take a factor display of length 1:
        # q[i] must be prime and > last_prime
        if is_prime(q[i]) and q[i] > last_prime:
            res += dfs(i+1, q[i])
            res %= MOD

        # Case 2: Take a factor display of length 2:
        # q[i] is prime > last_prime, q[i+1] is exponent >=2
        if i+1 < N:
            if is_prime(q[i]) and q[i] > last_prime:
                # exponent token can be any integer >=2 from constraints
                exponent = q[i+1]
                if exponent >= 2:
                    # Confirm q[i] ^ exponent is displayed as two tokens
                    # No extra check needed for the exponent's primality or anything else
                    res += dfs(i+2, q[i])
                    res %= MOD

        return res % MOD

    ans = dfs(0, 0) % MOD

    print(ans)

if __name__ == "__main__":
    main()