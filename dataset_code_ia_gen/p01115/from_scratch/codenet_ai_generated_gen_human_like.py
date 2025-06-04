import sys
import threading

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    while True:
        line = input()
        if not line:
            break
        n = line.strip()
        if n == '0':
            break
        n = int(n)
        s = input().strip()

        length = len(s)

        # To handle parentheses easily, we preprocess matching parenthesis pairs
        stack = []
        pairs = [-1]*length
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack:
                    open_idx = stack.pop()
                    pairs[open_idx] = i

        # We will parse the expression s in a top-down manner, memoizing results.
        # parse_E(l,r) parses s[l:r+1] as E and returns a list of tuples [(value, count, start, end)] of all parses for that substring 
        # but since s is a string expression, and substrings can be any substring, we only parse the whole s once,
        # and count substrings that form expressions equal to n afterwards.
        #
        # However, the problem asks to count substrings of s that are valid expressions and evaluate to n.
        # A substring can itself be an expression.
        # The direct parsing of every substring is too expensive (up to length 2M).
        #
        # We must parse s once and determine for each substring which values it can take.
        # The problem is challenging due to the huge length.
        #
        # The key insight: The expression is uniquely parsed by the grammar, so the expression is fully parenthesized according to operator precedence.
        # We can parse the expression structure once, and then count how many substrings correspond to expressions evaluating to n.
        #
        # The grammar:
        # E = E + T | T
        # T = T * F | F
        # F = digit or (E)
        #
        # For substring parsing, we consider each node in the parse tree and track all substrings corresponding to expressions.
        # For each node, we keep:
        # start index, end index, value
        #
        # Subexpressions correspond to contiguous substrings of s.
        #
        # So, we will:
        # 1) Parse s into the parse tree, remembering nodes with their span and value
        # 2) Each node is a valid expression substring, count those with value == n
        # 3) Also, consider substrings of s that cover sub-nodes
        #
        # Because the grammar is unambiguous, every substring that is a valid expression corresponds to some node in this parse tree.
        #
        # So counting nodes with value == n is enough.
        #
        # Proceed with recursive parsing functions returning a node that describes the expression subtree:
        # Each node: {start, end, value, type_of_node, children...}
        #
        # After building tree, traverse to count nodes with value == n.

        # Parsing functions will return a node with (start, end, value, children)
        # To parse efficiently, we implement a recursive descent parser with pointers.

        # The parser will parse s from l to r inclusive.

        # To avoid copying substrings, we'll parse by indices.

        pos = 0
        length = len(s)

        def parse_F():
            nonlocal pos
            # F ::= digit | '(' E ')'
            start_pos = pos
            if s[pos] == '(':
                # find matching ')'
                match_pos = pairs[pos]
                pos +=1
                node = parse_E()
                if pos != match_pos:
                    # Should not happen for valid input
                    pass
                pos += 1
                return {'start': start_pos, 'end': match_pos, 'value': node['value'], 'children':[node], 'type':'F'}
            else:
                # digit
                val = int(s[pos])
                end_pos = pos
                pos += 1
                return {'start': start_pos, 'end': end_pos, 'value': val, 'children':[], 'type':'F'}

        def parse_T():
            nonlocal pos
            node = parse_F()
            while pos < length and s[pos] == '*':
                op_pos = pos
                pos += 1
                right = parse_F()
                val = node['value'] * right['value']
                node = {'start': node['start'], 'end': right['end'], 'value': val, 'children':[node,right], 'type':'T'}
            return node

        def parse_E():
            nonlocal pos
            node = parse_T()
            while pos < length and s[pos] == '+':
                op_pos = pos
                pos += 1
                right = parse_T()
                val = node['value'] + right['value']
                node = {'start': node['start'], 'end': right['end'], 'value': val, 'children':[node,right], 'type':'E'}
            return node

        # parse whole expression
        pos = 0
        root = parse_E()

        # Now, all nodes formed above correspond to valid expression substrings.

        # We'll perform a DFS on this tree and count how many nodes have value == n.
        count = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node['value'] == n:
                count +=1
            stack.extend(node['children'])

        print(count)

threading.Thread(target=main).start()