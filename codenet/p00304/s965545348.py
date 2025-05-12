'''aizu 0309
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0309
'''
# encoding: 'utf-8'

N = 1000000007

def main():
    '''main func.
    '''

    node_n = int(input())
    nodes = list()
    for _ in range(node_n):
        nodes.append(Node(input()))
    for _ in range(node_n - 1):
        i, j = tuple([int(x) for x in input().split()])
        nodes[i-1].children.append(nodes[j-1])
        nodes[i-1].index.append(j-1)

    print(reduce_to_top(nodes).n % N)

def product(iterator):
    '''product for iterator
    '''
    result = 1
    for element in iterator:
        result *= element % N
        result %= N
    return result

def step_reducing(nodes):
    last_parents = [node for node in nodes if node is not None and node.is_last_parent()]
    for parent in last_parents:
        parent.n = parent.number_of_cases()
        parent.children = list()
        for i in parent.index:
            nodes[i] = None
    return nodes

def reduce_to_top(nodes):
    while nodes[1:] != [None]*(len(nodes)-1):
        nodes = step_reducing(nodes)
    return nodes[0]

class Node:
    '''Node class
    '''

    def __init__(self, kind, children=None, n=None, index=None):
        self.kind = kind
        if children is None:
            children = list()
        if index is None:
            index = list()
        self.children = children
        self.index = index
        self.n = None

    def number_of_cases(self):
        ''' calc the number of cases.
        '''
        if self.n is not None:
            return self.n

        cases = self.generate_cases()
        if "E" in self.kind:
            result = product(cases)
            if "?" in self.kind:
                result += 1
            return result % N

        elif "A" in self.kind:
            result = sum(cases)
            if "?" in self.kind:
                result += 1
            return result % N

        elif "R" in self.kind:
            result = product((x+1 for x in cases))
            if "?" not in self.kind:
                result -= 1
            return result % N

        else:
            raise Exception("unreachable.")

    def generate_cases(self):
        '''generate cases
        '''
        for child in self.children:
            yield child.number_of_cases()

    def is_last_parent(self):
        bools = [child.children == [] for child in self.children]
        return bools and all(bools)

if __name__ == '__main__':
    main()