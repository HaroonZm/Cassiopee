# Define a function named 'check' which takes a single argument 'a'
def check(a):
    # Initialize an empty list called 'path' to represent the current directory path as we process
    path = []
    # Iterate through each directory element in 'a', skipping the first character (assumed '/')
    # and splitting the path on the '/' character
    for d in a[1:].split("/"):
        # If the directory element is '.', it refers to the current directory and can be ignored
        if   d == ".":
            continue  # Skip processing for current directory
        # If the directory element is an empty string, it means there were two slashes (//), so use root directory
        elif d == "" :
            d = "/"  # Assign the root directory as a normalization step
        # If the directory element is '..', it refers to the parent directory
        elif d == "..":
            # If 'path' is empty, we can't go up, or the joined path isn't a valid prefix of any url in 'urls'
            if len(path) == 0 or max(url.find("/"+"/".join(path)+"/") for url in urls) == -1:
                return False  # Return False as going up isn't valid
            # Remove the last element from 'path' to go up one directory
            path.pop()
            continue  # Continue to next directory element
        # For any other directory element, add it to the 'path' list
        path.append(d)
    # Join the 'path' list into a url path, ensuring slashes are placed correctly
    url = ("/"+"/".join(path)).replace("//","/")
    # If the constructed 'url' exists in 'urls', it is valid and return it
    if url in urls:
        return url
    # If not found, try appending '/index.html' to the path (typical web default)
    url = (url+"/index.html").replace("//","/")
    # Return the new url if it exists in 'urls', otherwise False
    return url if url in urls else False

# Begin an infinite loop; will only stop when user enters 0 for 'n'
while 1:
    # Read a line from input, split into two integers n and m
    # n: number of urls to be entered
    # m: number of url pairs to be checked
    n,m = map(int,raw_input().split())
    # If n is 0, break out of the loop, ending the program
    if n == 0:
        break
    # Read 'n' lines of input to populate the 'urls' list; each is a valid url string
    urls = [raw_input() for i in xrange(n)]
    # For each of the 'm' pairs of checks:
    for loop in xrange(m):
        # Read the first string, use check() to process and normalize it to 'a'
        a = check(raw_input())
        # Read the second string, use check() to process and normalize it to 'b'
        b = check(raw_input())
        # If either 'a' or 'b' is False, meaning not found, print 'not found'
        if not (a and b):
            print "not found"
        # If both found, but the normalized urls aren't the same, print 'no'
        elif a != b:
            print "no"
        # If both are found and they are the same after normalization, print 'yes'
        else:
            print "yes"