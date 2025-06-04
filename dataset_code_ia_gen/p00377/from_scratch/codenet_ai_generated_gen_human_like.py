N, C = map(int, input().split())
cakes = list(map(int, input().split()))

total_cakes = sum(cakes)
total_people = N + 1  # friends + me

cakes_per_person = total_cakes // total_people
remainder = total_cakes % total_people

# Each person gets cakes_per_person pieces, host gets the remainder as well
host_cakes = cakes_per_person + remainder
print(host_cakes)