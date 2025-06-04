input_str = input()
result = ''

def get_c(x):
    return dict(zip("1234567890", ["", "k", "s", "t", "n", "h", "m", "y", "r", "w"])).get(x, "")

class Mapper:
    m = {"T":"a", "L":"i", "U":"u", "R":"e", "D":"o"}
    @staticmethod
    def get_m(y):
        return Mapper.m.get(y, "")

i = 0
while i < len(input_str):
    chunk = input_str[i:i+2]
    if chunk == '0U':
        result += "nn"
    else:
        result = "{}{}{}".format(result, get_c(chunk[0]), Mapper.get_m(chunk[1]))
    i += 2

print(result)