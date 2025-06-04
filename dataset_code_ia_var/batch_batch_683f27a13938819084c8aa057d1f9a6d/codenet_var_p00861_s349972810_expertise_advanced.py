from collections import defaultdict
import re
from functools import lru_cache

class CustomArray:
    __slots__ = ('sz', 'vals')
    def __init__(self, sz: int):
        self.sz = sz
        self.vals = {}

    def size(self):
        return self.sz

    def assign(self, idx, val):
        if idx is None or val is None or not (0 <= idx < self.sz):
            return False
        self.vals[idx] = val
        return True

    def get(self, idx):
        if idx is None or not (0 <= idx < self.sz):
            return None
        return self.vals.get(idx)

class Arrays(defaultdict):
    def __init__(self):
        super().__init__()
    
    def declare(self, arrName, sz):
        if sz is None or arrName in self:
            return False
        self[arrName] = CustomArray(sz)
        return True

    def assign(self, arrName, idx, val):
        arr = self.get(arrName)
        if arr is None:
            return False
        return arr.assign(idx, val)

    def get(self, arrName, idx):
        arr = self.get(arrName)
        return arr.get(idx) if arr else None

@lru_cache(maxsize=2000)
def resolve(expression):
    global arrays
    # Remove whitespace and handle numbers or nested array references
    exp = expression.strip()
    if "[" not in exp:
        try:
            return int(exp)
        except ValueError:
            return None
    m = re.match(r'^([A-Za-z])\[(.+)\]$', exp)
    if not m:
        return None
    arrName, inner = m.group(1), m.group(2)
    idx = resolve(inner)
    return arrays.get(arrName, idx)

def processAssignment(command):
    global arrays
    left, right = map(str.strip, command.split('=', 1))
    m = re.match(r'^([A-Za-z])\[(.+)\]$', left)
    if not m:
        return False
    arrName, idx_expr = m.group(1), m.group(2)
    leftIdx = resolve(idx_expr)
    rhs = resolve(right)
    return arrays.assign(arrName, leftIdx, rhs)

def processDeclaration(arrStr):
    global arrays
    m = re.match(r'^([A-Za-z])\[(.+)\]$', arrStr.strip())
    if not m:
        return False
    arrName, sz_expr = m.group(1), m.group(2)
    try:
        sz = int(sz_expr)
    except ValueError:
        return False
    return arrays.declare(arrName, sz)

if __name__ == '__main__':
    import sys
    input_stream = iter(sys.stdin.readline, '')
    while True:
        commands = []
        while True:
            line = next(input_stream).strip()
            if line == '.':
                break
            if line:
                commands.append(line)
        if not commands:
            break
        errLine = 0
        arrays = Arrays()
        resolve.cache_clear()
        for i, command in enumerate(commands):
            result = (processAssignment(command) if '=' in command else processDeclaration(command))
            if not result:
                errLine = i + 1
                break
        print(errLine)