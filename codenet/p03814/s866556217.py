import sys

s = input()

a_index = s.find("A")
z_index = s.rfind("Z")

print("{}".format(z_index - a_index + 1))