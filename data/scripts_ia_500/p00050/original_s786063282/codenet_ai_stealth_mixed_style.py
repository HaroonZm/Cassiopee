str = input()
def replace_fruits(s):
    s = s.replace("apple", "xxxxx")
    s = s.replace("peach", "apple")
    return s.replace("xxxxx", "peach")

result = replace_fruits(str)
print(result)