import sys

def parse_path(path):
    # Split path by '/' and filter empty elements
    return [seg for seg in path.split('/') if seg != '']

def build_files_and_dirs(n, files):
    dirs = set(['/'])
    files_set = set()
    for fpath in files:
        segments = parse_path(fpath)
        # Add all parent directories
        for i in range(len(segments)):
            dir_path = '/' + '/'.join(segments[:i])
            if dir_path == '':
                dir_path = '/'
            dirs.add(dir_path if dir_path.endswith('/') else dir_path+'/')
        file_path = '/' + '/'.join(segments)
        files_set.add(file_path)
    return files_set, dirs

def normalize_path(path, dirs):
    # Normalize path according to problem rules
    # Returns normalized absolute path to file or None if invalid
    # Steps:
    # 1) Split path by '/'
    # 2) Process segments, handle . and .. as directory names, but .. means move up dir unless root
    # 3) After normalization, handle index.html rule, trailing slash rule
    if path == '/':
        # root directory alone can only mean index.html directly under root (if exists)
        return '/'
    orig_path = path
    segments = path.strip('/').split('/')
    stack = []
    for seg in segments:
        if seg == '..':
            if len(stack) == 0:
                # cannot go above root directory
                return None
            # Check whether the parent directory exists or not?
            # According to problem, parent must exist
            stack.pop()
        elif seg == '.':
            # '.' means current directory, do nothing (treated as dir but no stack change)
            continue
        else:
            stack.append(seg)
    # Now build normalized path
    normalized = '/' + '/'.join(stack)
    # Determine if this means a directory or file
    # Last segment can be a file name or directory name
    # But problem says if last segment is 'index.html' (file), can be omitted,
    # so also if omitted, path may end with last segment directory if index.html exists in that dir
    # Here we try to find normalized file path
    # Step A: If path ends with '/', treat as directory path
    is_slash_ended = path.endswith('/')
    # 4 cases:
    # a) If path ends with 'index.html' then it's file path
    # b) If path ends with '/' - treat it as directory path, possibly index.html file in it
    # c) else treat it as directory or file in the rules below
    # Strategy:
    # Try to resolve to file path first
    # first try path as file:
    file_candidate = normalized
    if not file_candidate.startswith('/'):
        file_candidate = '/' + file_candidate
    # Assure no trailing slash for file
    if file_candidate.endswith('/'):
        file_candidate = file_candidate[:-1]
    # Check if this file exists
    if file_candidate in files_set:
        return file_candidate

    # If last segment not index.html and file_candidate not found, try index.html addition
    # if path ends with '/', try index.html in that directory
    if normalized == '/':
        # Root directory index.html
        idxpath = '/index.html'
    else:
        if normalized.endswith('/'):
            idxpath = normalized + 'index.html'
        else:
            idxpath = normalized + '/index.html'
    if idxpath in files_set:
        return idxpath

    # Try shorten form for file paths without ending slash but the file is index.html
    # Example: /ICPC instead /ICPC/index.html
    # So if last segment is directory, check if /dir/index.html exists
    if not is_slash_ended:
        if normalized in dirs:
            idxpath = normalized
            if not idxpath.endswith('/'):
                idxpath = idxpath + '/'
            idxpath += 'index.html'
            if idxpath in files_set:
                return idxpath

    return None

def add_trailing_slash_if_dir(path, dirs):
    # Returns path with trailing slash if directory and no trailing slash
    if path == '/':
        return '/'
    if path in dirs:
        if not path.endswith('/'):
            return path + '/'
    return path

input = sys.stdin.readline

while True:
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if line == '':
            break
    if not line:
        break
    N, M = map(int, line.strip().split())
    if N == 0 and M == 0:
        break
    file_paths = []
    for _ in range(N):
        f = sys.stdin.readline().strip()
        file_paths.append(f)
    files_set, dirs = build_files_and_dirs(N, file_paths)
    # Remove trailing slash from dirs for consistency, store with trailing slash
    # Actually, store dirs with trailing slash, file paths without trailing slash
    # Already ensured in build_files_and_dirs

    queries = []
    for _ in range(M*2):
        q = sys.stdin.readline().strip()
        queries.append(q)

    for i in range(M):
        p1 = queries[2*i]
        p2 = queries[2*i+1]
        res1 = normalize_path(p1, dirs)
        res2 = normalize_path(p2, dirs)
        if res1 is None or res2 is None:
            print("not found")
        elif res1 == res2:
            print("yes")
        else:
            print("no")