# Importing necessary functions; open() is used to access standard input (fd=0) and output (fd=1)
readline = open(0).readline  # Assign the 'readline' method from the file-object (standard input) to the variable 'readline'
writelines = open(1, 'w').writelines  # Assign the 'writelines' method from the file-object (standard output) to the variable 'writelines'

s = set()  # Create an empty set 's'. A set in Python is an unordered collection of unique elements.

def insert(x):
    """
    Inserts the element 'x' into the set 's'.
    If 'x' is already present, set does nothing, maintaining uniqueness.
    Returns a string with the current number of distinct elements (length of set), followed by a newline character.
    """
    s.add(x)  # Add 'x' to the set 's'. Duplicate elements are automatically ignored by the set.
    return "%d\n" % len(s)  # Format the number of unique elements in the set as a string followed by newline.

def find(x):
    """
    Checks if the element 'x' is in the set 's'.
    Returns '1\n' if 'x' is present, else '0\n'.
    """
    return "%d\n" % (x in s)  # (x in s) is a boolean (True=1, False=0). It is converted implicitly to int (1 or 0), then formatted.

# 'C' is a list where index 0 corresponds to 'insert', and index 1 corresponds to 'find'.
# '__getitem__' is used so that 'C(type)' retrieves either insert or find depending on 'type'.
C = [insert, find].__getitem__  # Assign the internal method '__getitem__' to C for efficient function selection.

Q = int(readline())  # Read a single line from stdin, strip newline, and convert to integer. Represents the number of queries to process.

ans = []  # Create an empty list 'ans' to store the results of all queries.

# Loop Q times. Each iteration processes one query.
for _ in range(Q):
    t, x = map(int, readline().split())  # Read one line, split by whitespace, map both strings to int, and unpack into 't' (type), 'x' (element)
    # 'C(t)' picks insert if t==0, or find if t==1; then it's called with parameter x. The result string is appended to 'ans'.
    ans.append(C(t)(x))

# Write all responses from 'ans' to standard output at once.
# 'writelines' expects a list of strings (each with '\n' already).
writelines(ans)