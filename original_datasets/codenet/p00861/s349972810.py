class CustomArray:
    def __init__(self, sz):
        self.sz = sz
        self.vals = {}

    def size(self):
        return self.sz

    def assign(self, idx, val):
        if idx == None or val == None:
            return False
        if idx >= self.sz:
            return False
        self.vals[idx] = val
        return True
    
    def get(self, idx):
        if idx == None:
            return None
        if idx >= self.sz:
            return None
        if idx not in self.vals:
            return None
        return self.vals[idx]

class Arrays:
    def __init__(self):
        self.arrays = {}

    def declare(self, arrName, sz):
        if sz == None:
            return False
        if arrName in self.arrays:
            return False
        self.arrays[arrName] = CustomArray(sz)
        return True

    def assign(self, arrName, idx, val):
        if arrName not in self.arrays:
            return False
        return self.arrays[arrName].assign(idx, val)

    def get(self, arrName, idx):
        if arrName not in self.arrays:
            return None
        return self.arrays[arrName].get(idx)
        
def resolve(expression):
    global arrays

    if "[" not in expression:
        return int(expression)

    arrName = expression[0]
    idx = resolve(expression[2:-1])

    return arrays.get(arrName, idx)

def processAssignment(command):
    global arrays

    equalIdx = command.find("=")
    leftStr = command[:equalIdx]
    rightStr = command[equalIdx + 1:]

    leftArrName = leftStr[0]
    leftIdx = resolve(leftStr[2:-1])
    rhs = resolve(rightStr)
    
    return arrays.assign(leftArrName, leftIdx, rhs)

def processDeclaration(arrStr):
    global arrays
    arrName = arrStr[0]
    sz = int(arrStr[2:-1])
    return arrays.declare(arrName, sz)

if __name__ == '__main__':
    while True:
        commands = []
        while True:
            line = input().strip()
            if line == '.':
                break
            commands.append(line)

        if len(commands) == 0:
            break

        errLine = 0
        arrays = Arrays()

        for i in range(len(commands)):
            command = commands[i]
            
            if "=" in command:
                result = processAssignment(command)
            else:
                result = processDeclaration(command)

            if not result:
                errLine = i + 1
                break

        print(errLine)