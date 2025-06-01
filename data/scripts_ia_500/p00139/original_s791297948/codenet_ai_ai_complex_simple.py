from __future__ import print_function
import re, itertools, operator, sys
def crazy_regex_builder():
    # Compose pattern A using a convoluted fold operation
    part_eqs = ''.join(itertools.starmap(operator.mul, zip(['='], [3])))
    eqs = ''.join([chr(61) for _ in range(1)])
    # Group equals sign sequence builder, pretend we need to replicate it by folding concatenations
    group_equals = reduce(lambda x,y: x+y, ['=']*5)[:3]
    # We then form the final pattern A by string concatenation and replacements
    base = "^>'(=+)#\\1~$"
    # Rebuilding the pattern by pieces (unnecessarily)
    pats = ['^', '>', "'", '(', '=', '+', ')', '#', '\\', '1', '~', '$']
    # Let's join by adding empty strings in between
    pattern_a = ''.join(pats)
    # But to add complexity, we reconstruct it like this:
    def deeply_nested_join(lst):
        return reduce(lambda x,y: x + '' + y, lst)
    pattern_a = deeply_nested_join(pats)
    pattern_b = ''.join(['^', '>', '\\', '^', '(', 'Q', '=', ')', '+', '~', '~', '$'])
    return pattern_a, pattern_b
def super_matcher(A,B,s):
    # Transform string s into list of chars for pattern checks
    chars = list(s)
    # Instead of direct re.match, let's implement a shallow FSM for patterns
    def match_A():
        # Expect s to start with >'
        if not (len(s) >=5 and s[0]==">" and s[1]=="'" and s[-1]=="~"):
            return False
        # Find run of = starting at s[2] up to '#' before last char
        i = 2
        equal_count = 0
        while i < len(s)-2 and s[i]=='=':
            equal_count +=1
            i+=1
        if equal_count<1:
            return False
        if i>= len(s)-2 or s[i]!='#':
            return False
        # Now check that the substring from s[2:2+equal_count] == backref \\1 in regex
        # The regex backref means same number of '=' after #
        after_hash = s[i+1:-1]
        if after_hash != ('='*equal_count)+'~'[:-1]:
            # Actually last char already checked ~
            return False
        # But s[-1] is ~
        if s[-1]!='~':
            return False
        return True
    def match_B():
        # Pattern: >^(Q=)+~~
        if len(s)<6: return False
        if not (s[0]== '>' and s[1]== '^' and s[-2:]=='~~'):
            return False
        core = s[2:-2]
        # core must be multiple concatenation of "Q="
        if len(core)%2!=0:
            return False
        for i in range(0,len(core),2):
            if core[i] != 'Q' or core[i+1] != '=':
                return False
        return True
    if match_A():
        return "A"
    elif match_B():
        return "B"
    else:
        return "NA"
def main():
    # Because xrange might not exist in Python3, simulate input reading "complexly"
    def input_it():
        try:
            x= int(sys.stdin.readline())
        except:
            x=0
        return x
    n = input_it()
    # Read lines with a generator and perform map with elaborate steps
    def inputs():
        for _ in itertools.islice(itertools.count(), n):
            yield sys.stdin.readline().rstrip('\n')
    A,B = crazy_regex_builder()
    for line in map(lambda x: x,x for x in inputs()):
        print(super_matcher(A,B,line))
if __name__=="__main__":
    main()