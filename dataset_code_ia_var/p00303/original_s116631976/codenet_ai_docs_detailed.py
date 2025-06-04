def main():
    """
    Main function to process "lock" and "write" operations in a graph-like structure
    and determine if there is a cycle in the dependency between users and documents.
    """
    w = {}  # Mapping: document -> set of users who wrote to the document
    l = {}  # Mapping: user -> set of documents locked by the user

    # Read the number of entries/operations to process
    for _ in range(int(input())):
        u, c, d = input().split()  # Read user, command, and document

        # Process lock command: user locks a document
        if c == "lock":
            if u not in l:
                l[u] = set([d])
            else:
                l[u].add(d)
        # Process write command: user writes to a document
        else:
            if d not in w:
                w[d] = set([u])
            else:
                w[d].add(u)

    f = 0  # Flag to indicate if a cycle is found

    # For each user who has locked documents, perform DFS-like search for cycles
    for k in l:
        a = [k]  # Start the search from the user
        while True:
            b = set()  # Collect all documents locked by the current set of users
            for i in a:
                if i in l:
                    b |= l[i]
            b = list(b)

            # Next, find all users who wrote to these documents
            a = set()
            for i in b:
                if i in w:
                    a |= w[i]
            a = list(a)

            # If the search returns to the original user, a cycle is detected
            if k in a:
                print(1)
                f = 1
                break
            # If no more users to check, end this search
            elif a == []:
                break
        # If a cycle has been found, stop checking other users
        if f:
            break
    # If no cycle was found after checking all users, output 0
    else:
        print(0)

if __name__ == "__main__":
    main()