height = []

for apple in range(10):
	mountain = input()
	height.insert(-1, mountain)
	
height.sort()
height.reverse()

print height[0]
print height[1]
print height[2]