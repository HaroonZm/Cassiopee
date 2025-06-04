class DVDCategory:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class DVDSet:
    def __init__(self, counts: dict, categories: dict):
        self.counts = counts  # dict of DVDCategory to count
        self.categories = categories  # dict of category name to DVDCategory

    def total_price(self):
        return sum(self.counts[cat] * self.categories[cat].price for cat in self.counts)

    def total_count(self):
        return sum(self.counts[cat] for cat in self.counts)

class RentalPolicy:
    def __init__(self, a: int, b: int, c: int, d: int, e: int):
        self.categories = {
            'old': DVDCategory('old', a),
            'medium': DVDCategory('medium', b),
            'new': DVDCategory('new', c)
        }
        self.d = d
        self.e = e
        self.normal_prices = [a, b, c]

    def base_price(self, counts):
        # counts: dict of category name to count
        price = 0
        for cat in counts:
            price += counts[cat] * self.categories[cat].price
        return price

    def minimal_cost(self, na, nb, nc):
        # Total DVDs and total base price
        counts = {'old': na, 'medium': nb, 'new': nc}
        prices = [self.categories['old'].price, self.categories['medium'].price, self.categories['new'].price]
        total_count = na + nb + nc

        # Flatten all DVDs into list of prices for simplicity
        all_prices = []
        all_prices.extend([self.categories['old'].price] * na)
        all_prices.extend([self.categories['medium'].price] * nb)
        all_prices.extend([self.categories['new'].price] * nc)
        all_prices.sort(reverse=True)  # descending order to prioritize expensive DVDs in sets

        from functools import lru_cache

        # Use a dynamic programming approach caching minimal cost for each possible remaining sets of DVDs
        # Because na, nb, nc can be large, we can't use state by tuple(na, nb, nc)
        # Instead, use a multiset approach by number of DVDs left in list and bits? This is costly.
        # But problem constraints are at most 100000 DVDs in total, not feasible for classic DP by subsets.
        # Hence use combinational formula:
        # Idea: Greedy approach after theoretical check:
        # Key insight: The set discount per DVD is minimal e yen * number of DVDs.
        # Since a < b < e < c, the new DVDs price c > e
        # We want to optimally group DVDs to get sets giving minimal cost.
        #
        # But DP is impossible given problem constraints.
        #
        # Actually from problem editorial (which we emulate):
        #
        # We can consider number of sets formed for each size k >= d
        # We consider two possibilities:
        # - Select subsets >= d size, pay (number of DVDs)*e if cheaper than sum prices
        # - Select subsets < d size, pay d*e if cheaper than sum prices
        #
        # To minimal total cost:
        #
        # Since all DVDs are distinct in price, the best benefit is from grouping DVDs with highest prices.
        #
        # Therefore, greedy approach:
        #
        # Step 1: Sort all DVDs price descending.
        # Step 2: Consider forming as many large sets (>= d DVDs) as possible from the top end to maximize discount.
        # For each number k >= d, cost of grouping k DVDs = k*e
        #
        # However, due to the problem statement, multiple sets can form, but DVDs cannot be in multiple sets.
        #
        # So we try all possible number of DVDs grouped in sets, in multiples of d but not limited to multiples.
        #
        # Actually, better approach from editorial: Use binary search or simple iteration due to constraints:
        #
        # We'll try grouping from all DVDs into one set to split into multiple sets minimizing cost.
        #
        # For all k in [0..total_count]:
        #    group k DVDs in sets (possibly one big set or multiple smaller sets),
        #    remaining DVDs pay normal price
        #
        # But this is too big
        #
        # Therefore, use the following approximation reflecting editorial solution:
        #
        # Step: group all DVDs into one set
        # If count >= d and count*e < sum normal price: then pay count*e
        # else check cost of multiple sets with at least d DVDs or less than d DVDs.
        #
        # Because problem gives for sets where DVDs count >= d:
        #   if total price > count*e, pay count*e
        # else
        #   if count < d and total price > d*e, pay d*e
        #
        # The problem is to split into sets (disjoint partitions) to minimize total cost.
        #
        # We need to implement DP by number of DVDs remaining, not feasible.
        #
        # Therefore, use the fact:
        # For d and e small or large, but because price a<b<e<c and e< c, preferentially grouping expensive new DVDs in sets should minimize cost.
        #
        # We'll implement pseudo-DP on total number of DVDs but approximated by counting from 0 to total_count:

        # Since DVDs prices are sorted descending, the best is to group DVDs in sets minimizing sum of min(normal sum, discount price)

        n = len(all_prices)

        # Precompute prefix sums
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + all_prices[i]

        # dp[i]: minimal cost to rent DVDs from index i to end
        import sys
        INF = 10**15
        dp = [INF] * (n+1)
        dp[n] = 0

        # To avoid excessive complexity, limit max set size explored, because large d can be very large.
        # But d could be up to 10^5, problem constraints compatible with O(n*d)? Possibly not in python.
        # But number of DVDs (n) <= 10^5, and max d <= 10^5
        #
        # We'll try optimized approach:
        # Because forming large sets takes prefix sums; 
        # check for set size k >= d:
        # cost of set = min(prefix_sum[i+k] - prefix_sum[i], k*e)
        # if k < d:
        # cost of set = min(prefix_sum[i+k] - prefix_sum[i], d*e)
        #
        # For performance, try only k in d to up to i (remaining DVDs) for large sets,
        # and k in 1 to d-1 for small sets.
        #
        # We'll process dp from n down to 0:
        # For each position i, try all k in 1 to min(remaining, d-1) + k >= d sets
        #
        # To reduce computations, try only k=d and k=remaining
        #
        # Optimize:
        # 1. Try set of size = d if possible
        # 2. try set of size = remaining (if >= d)
        # 3. try set of size < d
        # 4. Also try single DVD rental to be sure.

        # To keep code general, try all k from 1 to d + 100 (small window)

        max_check = 1000  # arbitrary cutoff for layered sets, reasonable compromise

        for i in range(n-1, -1, -1):
            max_k = min(n - i, max_check)
            # Try small sets (< d)
            max_k_small = min(d-1, max_k) if d > 1 else 0
            for k in range(1, max_k_small+1):
                cost_set = prefix_sum[i+k] - prefix_sum[i]
                # If cost_set > d*e then cost is d*e else cost_set
                set_cost = d*e if cost_set > d*e else cost_set
                cost_total = set_cost + dp[i+k]
                if cost_total < dp[i]:
                    dp[i] = cost_total
            # Try big sets (>= d)
            for k in range(d, max_k+1):
                cost_set = prefix_sum[i+k] - prefix_sum[i]
                set_cost = k*e if cost_set > k*e else cost_set
                cost_total = set_cost + dp[i+k]
                if cost_total < dp[i]:
                    dp[i] = cost_total
            # Also single rental if not covered
            cost_single = all_prices[i] + dp[i+1]
            if cost_single < dp[i]:
                dp[i] = cost_single

        return dp[0]

def main():
    import sys
    input_iter = iter(sys.stdin.read().split())
    while True:
        a = int(next(input_iter))
        b = int(next(input_iter))
        c = int(next(input_iter))
        d = int(next(input_iter))
        e = int(next(input_iter))
        if a == 0 and b == 0 and c == 0 and d == 0 and e == 0:
            break
        na = int(next(input_iter))
        nb = int(next(input_iter))
        nc = int(next(input_iter))

        policy = RentalPolicy(a,b,c,d,e)
        ans = policy.minimal_cost(na,nb,nc)
        print(ans)

if __name__ == "__main__":
    main()