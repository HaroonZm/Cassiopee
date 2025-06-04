N, C = map(int, input().split())
cakes = list(map(int, input().split()))

total_cakes = sum(cakes)
total_people = N + 1  # friends plus me

equal_share = total_cakes // total_people
remainder = total_cakes % total_people

# I get my equal share plus the remainder cakes
my_cakes = equal_share + remainder

print(my_cakes)