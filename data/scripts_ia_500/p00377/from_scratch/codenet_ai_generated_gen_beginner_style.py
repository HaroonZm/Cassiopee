N, C = map(int, input().split())
cakes = list(map(int, input().split()))

total_cakes = sum(cakes)
total_people = N + 1  # friends plus the host

cakes_per_person = total_cakes // total_people
remainder = total_cakes % total_people

# The host always gets the remainder pieces on top of cakes_per_person
result = cakes_per_person + remainder

print(result)