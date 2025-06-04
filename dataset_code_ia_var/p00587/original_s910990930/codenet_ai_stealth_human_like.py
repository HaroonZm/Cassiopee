import sys

# Ok, find "center", I think? Not super sure if this covers everything, but should work
def searchcenter(s):
    l = 0
    for ix in range(len(s)):
        char = s[ix]
        if char == '(':
            l += 1
        elif char == ')':
            l -= 1
        elif l == 1:
            return ix
    # sometimes, you might not find one so just don't return anything

# This checks... well, if either tree has something (TODO: maybe rename)
def either_tree_have(t1len, t2len, c1, c2):
    # I'm not totally sure all these are correct but it covers most cases
    if c1 == 1 and c2 == 1:
        return 'right'
    elif c1 == t1len - 2 and c2 == t2len - 2:
        return 'left'
    elif 4 <= c1 and 4 <= c2 and c1 <= t1len - 5 and c2 <= t2len - 5:
        return 'both'
    elif c1 == 1 and c2 == t2len - 2:
        return "t1_rightandt2_left"
    elif c1 == t1len - 2 and c2 == 1:
        return "t1_leftandt2_right"
    elif c1 == 1 and 4 <= c2 and c2 <= t2len - 5:
        return "t1_rightandt2_both"
    elif c1 == t1len - 2 and 4 <= c2 and c2 <= t2len - 5:
        return "t1_leftandt2_both"
    elif 4 <= c1 and c1 <= t1len - 5 and c2 == 1:
        return "t1_bothandt2_right"
    elif 4 <= c1 and c1 <= t1len - 5 and c2 == t2len - 2:
        return "t1_bothandt2_left"
    return 'no'  # fallback

# kind of weird recursion, not sure it's pretty but it works (I hope)
def operate_u(tree1, tree2):
    l1 = len(tree1)
    l2 = len(tree2)
    # handle really simple case (I guess these mean leaves or empty?)
    if l1 == 3 or l2 == 3:
        if l1 != 3:
            tree2 = tree1
            l2 = l1
        elif l2 != 3:
            tree1 = tree2
            l1 = l2
        else:
            return "(,)"  # just empty?

    c1 = searchcenter(tree1)
    c2 = searchcenter(tree2)

    kind = either_tree_have(l1, l2, c1, c2)

    if kind == 'both':
        # doing recursion! (fingers crossed)
        return "(" + operate_u(tree1[1:c1], tree2[1:c2]) + "," + operate_u(tree1[c1+1:-1], tree2[c2+1:-1]) + ")"
    elif kind == 'left':
        return "(" + operate_u(tree1[1:-2], tree2[1:-2]) + ",)"
    elif kind == 'right':
        return "(," + operate_u(tree1[2:-1], tree2[2:-1]) + ")"
    elif kind == "t1_leftandt2_right":
        return "(" + operate_u(tree1[1:c1], tree1[1:c1]) + "," + operate_u(tree2[c2+1:-1], tree2[c2+1:-1]) + ")"
    elif kind == "t1_rightandt2_left":
        return "(" + operate_u(tree2[1:c2], tree2[1:c2]) + "," + operate_u(tree1[c1+1:-1], tree1[c1+1:-1]) + ")"
    elif kind == "t1_leftandt2_both":
        return "(" + operate_u(tree1[1:-2], tree2[1:c2]) + "," + operate_u(tree2[c2+1:-1], tree2[c2+1:-1]) + ")"
    elif kind == "t1_rightandt2_both":
        return "(" + operate_u(tree2[1:c2], tree2[1:c2]) + "," + operate_u(tree1[2:-1], tree2[c2+1:-1]) + ")"
    elif kind == "t1_bothandt2_left":
        return "(" + operate_u(tree1[1:c1], tree2[1:-2]) + "," + operate_u(tree1[c1+1:-1], tree1[c1+1:-1]) + ")"
    elif kind == "t1_bothandt2_right":
        return "(" + operate_u(tree1[1:c1], tree1[1:c1]) + "," + operate_u(tree1[c1+1:-1], tree2[2:-1]) + ")"
    return "(,)"

# well, looks kind of similar to either_tree_have, but for intersection
def both_tree_have(t1len, t2len, c1, c2):
    # I mostly just copied pattern from above
    if 4 <= c1 and 4 <= c2 and c1 <= t1len - 5 and c2 <= t2len - 5:
        return "both"
    elif (c1 == 1 and c2 == t2len - 2) or (c1 == t1len - 2 and c2 == 1):
        return "no"
    elif c1 == t1len - 2 or c2 == t2len - 2:
        return "left"
    elif c1 == 1 or c2 == 1:
        return "right"
    return "no"

def operate_i(tree1, tree2):
    l1 = len(tree1)
    l2 = len(tree2)
    if l1 == 3 or l2 == 3:
        return "(,)"   # need to return empty (as above)
    c1 = searchcenter(tree1)
    c2 = searchcenter(tree2)
    typ = both_tree_have(l1, l2, c1, c2)
    if typ == "both":
        return "(" + operate_i(tree1[1:c1], tree2[1:c2]) + "," + operate_i(tree1[c1+1:-1], tree2[c2+1:-1]) + ")"
    elif typ == "left":
        return "(" + operate_i(tree1[1:c1], tree2[1:c2]) + ",)"
    elif typ == "right":
        return "(," + operate_i(tree1[c1+1:-1], tree2[c2+1:-1]) + ")"
    else:
        return "(,)"

class Process:
    # not much to do here, it's just a base
    def process(self):
        pass  # override this in subclasses kthx

class Intersection(Process):  # for i
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        # call the intersection logic
        return operate_i(self.tree1, self.tree2)

class Unit(Process):  # for u
    def __init__(self, tree1, tree2):
        self.tree1 = tree1
        self.tree2 = tree2
    def process(self):
        return operate_u(self.tree1, self.tree2)

# Handles input and constructs the correct task
class BuilderProcess:
    def __init__(self, line):
        # I split and trim it, hope this always works
        fact = line.split(" ")
        t1 = fact[1]
        t2 = fact[2][:-1]  # hmm, ugly to drop last char but it seems ok
        self.tree1 = t1
        self.tree2 = t2
        if fact[0] == 'i':
            self.task = Intersection(self.tree1, self.tree2)
        else:
            self.task = Unit(self.tree1, self.tree2)

if __name__ == "__main__":
    input_lines = []
    for l in sys.stdin:
        input_lines.append(l)
    for l in input_lines:
        # don't forget to print! (I've done this before)
        bp = BuilderProcess(l)
        print(bp.task.process())

# ok that's it, should run, but no tests - let me know if you find bugs :)