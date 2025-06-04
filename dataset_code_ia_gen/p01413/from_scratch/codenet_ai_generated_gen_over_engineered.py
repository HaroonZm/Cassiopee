class Product:
    def __init__(self, name: str, weight: int, sell_price: int):
        self.name = name
        self.weight = weight
        self.sell_price = sell_price

class MarketProduct:
    def __init__(self, product: Product, buy_price: int):
        self.product = product
        self.buy_price = buy_price
        self.profit = product.sell_price - buy_price

class City:
    def __init__(self, idx: int, x: int, y: int, market_products: list):
        self.idx = idx
        self.x = x
        self.y = y
        self.market_products = market_products

    def distance_to_market(self) -> int:
        # Manhattan distance to market at (0,0)
        return abs(self.x) + abs(self.y)

from functools import lru_cache
from typing import Dict, Tuple, List

class TradingQuest:
    def __init__(self, N: int, M: int, W: int, T: int,\
                 products_data: List[Tuple[str,int,int]], cities_data: List[Tuple[int,int,int,List[Tuple[str,int]]]]):
        # Initialize products dict: name -> Product
        self.products: Dict[str, Product] = {}
        for name, weight, sell_price in products_data:
            self.products[name] = Product(name, weight, sell_price)

        # Initialize cities list
        self.cities: List[City] = []
        for idx, (L, X, Y, items) in enumerate(cities_data, start=1):
            market_products = []
            for r_name, q_price in items:
                product = self.products[r_name]
                mp = MarketProduct(product, q_price)
                market_products.append(mp)
            city = City(idx, X, Y, market_products)
            self.cities.append(city)

        self.N = N
        self.M = M
        self.W = W
        self.T = T

        self.market_x = 0
        self.market_y = 0

        # Precompute distances city <-> market
        self.city_to_market_dist = [abs(city.x) + abs(city.y) for city in self.cities]

        # For DP: cache max profit for time used and inventory (represented abstractly)
        # But we do not track inventory per se; we assume instant buy/sell at city/market
        # We plan route as: from market to some cities buy some products, back to market and sell, repeat.

        # We will generate all possible product load-outs per city that fit weight W and yield profit>0.
        # To simplify, we consider buying one type of product maximum allowed per trip (since unlimited stock).
        # We then consider trips: market->city->market with profitable load.

        # For sophistication, let's encapsulate possible purchases per city, with all combinations.

        # We'll build all possible loadouts per city
        self.city_loadouts = []
        for city in self.cities:
            loadouts = self.generate_loadouts(city)
            self.city_loadouts.append(loadouts)

    def generate_loadouts(self, city: City):
        # Generate all combos of products sold in this city with profit>0, that fit in weight limit W.
        # Because M<=7, L_j<=M, and W can be big, we use DP for knapsack of profits with weight limit W.
        # However profit per unit = sell_price - buy_price:
        # We want to maximize profit per trip for city visit.

        # First filter products with profit>0
        products = [mp for mp in city.market_products if mp.profit > 0]
        if not products:
            return []  # no profitable products here

        # Define dp[w] = max profit with weight <= w from these products (unbounded knapsack)
        dp = [0]*(self.W+1)
        for mp in products:
            w = mp.product.weight
            p = mp.profit
            # Unbounded knapsack update
            for weight in range(w, self.W+1):
                val = dp[weight - w] + p
                if val > dp[weight]:
                    dp[weight] = val

        # We find max profit achievable for city
        max_profit = max(dp)

        # To be able to reconstruct loadout, we store one of them. For sophistication, store multiple.
        # But complexity, we store only the best profit loadout here and its weight.

        # Find min weight for max_profit
        min_weight = next(w for w, val in enumerate(dp) if val == max_profit)

        return [(min_weight, max_profit)]

    def solve(self):
        # Strategy: Dynamic programming over time.
        # Each trip from market->city->market costs 2*distance(city, market) minutes.
        # We can repeat trips to same or different cities with profits given.

        # We'll make a list of all possible trips:
        # Each trip: time_cost, profit

        trips = []
        for idx, city in enumerate(self.cities):
            dist = self.city_to_market_dist[idx]
            time_cost = 2*dist
            loadouts = self.city_loadouts[idx]
            for (weight, profit) in loadouts:
                if time_cost <= self.T and profit > 0:
                    trips.append((time_cost, profit))

        # Now solve unbounded knapsack with time as capacity and profit as value
        # dp[t] = max profit achievable within time t
        dp = [0]*(self.T+1)
        for t in range(1,self.T+1):
            best = dp[t-1]
            for cost, profit in trips:
                if cost <= t:
                    candidate = dp[t - cost] + profit
                    if candidate > best:
                        best = candidate
            dp[t] = best

        return dp[self.T]

def main():
    import sys
    input = sys.stdin.readline
    N,M,W,T = map(int, input().split())
    products_data = []
    for _ in range(M):
        s,v,p = input().split()
        v = int(v)
        p = int(p)
        products_data.append((s,v,p))
    cities_data = []
    for _ in range(N):
        L,x,y = input().split()
        L = int(L)
        x = int(x)
        y = int(y)
        items = []
        for __ in range(L):
            r,q = input().split()
            q = int(q)
            items.append((r,q))
        cities_data.append((L,x,y,items))

    quest = TradingQuest(N,M,W,T,products_data,cities_data)
    ans = quest.solve()
    print(ans)

if __name__ == "__main__":
    main()