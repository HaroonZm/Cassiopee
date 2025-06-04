import sys
import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.sqrt(x))
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True

def main():
    input_line = sys.stdin.readline().strip()
    n, c = input_line.split()
    n = int(n)
    c = int(c)

    # For n pairs (b_i, g_i), we need to find digits for these pairs
    # such that the constructed number is maximal under problem rules.
    # Since pairs must carry identical digits and order is:
    #     b1 b2 ... bn [c] gn ... g2 g1 (g reversed)
    # The digits for b and g must match per pair.
    # We want to output a number (string) accordingly.
    # The best approach:
    #   - Try digits from 9 to 0 to assign to pairs.
    #   - For each pair, assign the largest available digit d (0-9)
    #   - Construct number and check primality.
    #   - Try both including c (if c>=0) and excluding c (if c<0)
    #   - Choose the number that "does not lose":
    #     1. If prime && opponent not prime => win
    #     2. If both prime or both not prime => larger number wins
    #
    # Since no opponent number is given, the problem wants to output a number
    # that would not lose against any other number constructed similarly.
    # This essentially means outputting the largest prime number possible
    # with the construction rules, or if none prime, the largest number.
    #
    # We can generate all possible assignments of digits to n pairs
    # (each digit from 0..9), but that's 10^n, too large when n=10.
    #
    # So we use a heuristic: 
    #   - Try digits from 9 down to 0 for all pairs (same digit for all pairs)
    #     Note: pairs can have different digits, but since problem allows
    #     choosing any digit per pair, we try to maximize the number.
    #
    # However, problem examples suggest choosing all pairs the same digit
    # doesn't always work. So we try to generate digits representing a
    # palindrome considering the condition b's and g's correspond.
    #
    # We'll try to assign digits from high to low per pair, generate number
    # and test primality.
    
    # We'll produce all candidate numbers this way:
    # - For each possible digit combination for b (length n)
    #   - For each digit d_i in b, g_i = d_i (same digit)
    # - Number is b1 b2 ... bn [c if c>=0] gn ... g2 g1
    # - Must not start with 0, and last digit (g1) not 0 (to avoid leading 0 of reversed side)
    #
    # Since brute force over 10^10 is impossible, we apply a backtracking with pruning:
    # We try to build the digits from most significant (b1) to least significant (b_n)
    # and prune impossible paths:
    #
    # We will implement backtracking to find the largest number satisfying rules:
    # - b1 != 0 and g1 != 0
    # - combined number no leading zero
    # - number formed is prime or maximal
    
    # We test with and without c depending on c value

    # Since problem is complex, and time limited, implement a backtracking to find best number.

    best_num = None
    best_prime = False

    # Helper to build full number string from b digits, c, and g digits reversed
    def build_number(b_digits, c_digit):
        g_digits = b_digits[::-1]
        if c_digit >= 0:
            num_str = ''.join(str(d) for d in b_digits) + str(c_digit) + ''.join(str(d) for d in g_digits)
        else:
            num_str = ''.join(str(d) for d in b_digits) + ''.join(str(d) for d in g_digits)
        return num_str

    # Check leading zeros:
    # num_str cannot start with '0' or end with '0'
    # The first digit is b1, last digit is g1
    # So b_digits[0] != 0 and b_digits[-1] != 0.
    # Also, the problem forbids outputs starting with 0, so strictly no leading zero overall

    def valid_digits(b_digits):
        if b_digits[0] == 0:
            return False
        if b_digits[-1] == 0:
            return False
        return True

    # Backtracking to find best number
    from itertools import product

    # Because 10^n is too big, try to only check at most a subset:
    # We'll try all digit combos with digits in descending order to get maximum:
    # For each pair, try digits 9 to 0
    # We'll limit the number of candidates to check by pruning

    # We'll implement a DFS with early pruning, choosing highest digit per position first

    def dfs(pos, b_digits):
        nonlocal best_num, best_prime
        if pos == n:
            if not valid_digits(b_digits):
                return
            num_str = build_number(b_digits, c)
            if num_str[0] == '0' or num_str[-1] == '0':
                return
            num = int(num_str)
            prime = is_prime(num)
            if prime:
                if not best_prime or (best_prime and num > int(best_num)):
                    best_num = num_str
                    best_prime = True
            else:
                if not best_prime:
                    if best_num is None or num > int(best_num):
                        best_num = num_str
            return

        # try digits from 9 down to 0
        for d in range(9, -1, -1):
            b_digits.append(d)
            # pruning: if first digit zero at pos=0, skip
            if pos == 0 and d == 0:
                b_digits.pop()
                continue
            # later pruning on last digit will happen at end
            dfs(pos + 1, b_digits)
            b_digits.pop()

    dfs(0, [])

    # If c<0, try also same without c - to check if better number possible
    if c < 0:
        # try without c means c = -1 in build_number
        best_num_wo_c = None
        best_prime_wo_c = False

        def dfs_wo_c(pos, b_digits):
            nonlocal best_num_wo_c, best_prime_wo_c
            if pos == n:
                if not valid_digits(b_digits):
                    return
                num_str = build_number(b_digits, -1)
                if num_str[0] == '0' or num_str[-1] == '0':
                    return
                num = int(num_str)
                prime = is_prime(num)
                if prime:
                    if not best_prime_wo_c or (best_prime_wo_c and num > int(best_num_wo_c)):
                        best_num_wo_c = num_str
                        best_prime_wo_c = True
                else:
                    if not best_prime_wo_c:
                        if best_num_wo_c is None or num > int(best_num_wo_c):
                            best_num_wo_c = num_str
                return
            for d in range(9, -1, -1):
                b_digits.append(d)
                if pos == 0 and d == 0:
                    b_digits.pop()
                    continue
                dfs_wo_c(pos + 1, b_digits)
                b_digits.pop()

        dfs_wo_c(0, [])

        # Compare best with c and best without c
        # According to rules:
        # If prime vs nonprime: prime wins
        # both prime or both nonprime: larger number wins
        # We want not to lose, so take best accordingly.

        # So pick best prime number, or max number if no prime.

        if best_prime and best_prime_wo_c:
            # both prime, pick larger number
            if int(best_num_wo_c) > int(best_num):
                best_num = best_num_wo_c
                best_prime = True
        elif best_prime_wo_c and not best_prime:
            best_num = best_num_wo_c
            best_prime = True
        elif not best_prime_wo_c and not best_prime:
            # both non prime pick max
            if best_num_wo_c is not None:
                if int(best_num_wo_c) > int(best_num):
                    best_num = best_num_wo_c

    print(best_num)

if __name__ == "__main__":
    main()