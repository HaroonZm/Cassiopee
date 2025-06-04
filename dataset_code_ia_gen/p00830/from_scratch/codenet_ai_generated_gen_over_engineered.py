from typing import List, Tuple, Optional, Dict, Set, Union
import sys

class PathSegment:
    """
    Represents a single segment of a pathname.
    It keeps a name and can represent special segments '.' or '..' as normal directory names.
    """
    __slots__ = ('name',)
    def __init__(self, name: str):
        self.name = name
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, PathSegment):
            return False
        return self.name == other.name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def is_current_dir(self) -> bool:
        return self.name == '.'
    
    def is_parent_dir(self) -> bool:
        return self.name == '..'

    def __repr__(self):
        return f"Segment({self.name})"

class Pathname:
    """
    Represents an absolute pathname composed of path segments.
    It supports normalization according to special rules in the problem.
    """
    __slots__ = ('raw_path', 'segments', 'has_trailing_slash')
    
    def __init__(self, raw_path: str):
        self.raw_path = raw_path
        self.has_trailing_slash = raw_path.endswith('/')
        self.segments = self._parse_segments(raw_path)

    def _parse_segments(self, path: str) -> List[PathSegment]:
        # absolute path starting with '/'
        # convert to segments, ignoring empty segments between '//' (not allowed per problem)
        segments_str = path.strip('/')
        if segments_str == '':
            return []
        parts = segments_str.split('/')
        return [PathSegment(part) for part in parts]

    def __repr__(self):
        return f"Pathname({self.raw_path})"

class DirectoryTreeNode:
    """
    Node in a tree representing directory file system structure.
    Stores child directories and files.
    """
    __slots__ = ('name', 'parent', 'directories', 'files')
    def __init__(self, name: str, parent: Optional['DirectoryTreeNode'] = None):
        self.name = name
        self.parent = parent
        self.directories: Dict[str, DirectoryTreeNode] = {}
        self.files: Set[str] = set()
    
    def add_directory(self, dirname: str) -> 'DirectoryTreeNode':
        if dirname not in self.directories:
            self.directories[dirname] = DirectoryTreeNode(dirname, self)
        return self.directories[dirname]
    
    def add_file(self, filename: str):
        self.files.add(filename)
    
    def has_directory(self, dirname: str) -> bool:
        return dirname in self.directories
    
    def has_file(self, filename: str) -> bool:
        return filename in self.files

    def get_directory(self, dirname: str) -> Optional['DirectoryTreeNode']:
        return self.directories.get(dirname)
    
    def get_parent(self) -> Optional['DirectoryTreeNode']:
        return self.parent

    def __repr__(self):
        return f"Dir({self.name}, dirs={list(self.directories.keys())}, files={list(self.files)})"

class FileSystemModel:
    """
    Models the file system from input paths.
    Supports lookup of directories and files.
    """
    def __init__(self):
        self.root = DirectoryTreeNode('/')
    
    def add_path(self, pathname: Pathname):
        # All input pages are guaranteed to have no '.' or '..' as path segments
        # and end with a file (last segment is a file under the directory path)
        curr = self.root
        # last segment is a file name
        if not pathname.segments:
            # path like '/'
            return
        for segment in pathname.segments[:-1]:
            curr = curr.add_directory(segment.name)
        last_seg = pathname.segments[-1]
        curr.add_file(last_seg.name)
    
    def directory_exists(self, path_segments: List[str]) -> bool:
        """
        Check if given path_segments (directory names) corresponds to an existing directory.
        """
        curr = self.root
        for seg in path_segments:
            if not curr.has_directory(seg):
                return False
            curr = curr.get_directory(seg)
        return True
    
    def file_exists(self, path_segments: List[str], filename: str) -> bool:
        """
        Check if given directory path + filename exists as a file.
        """
        curr = self.root
        for seg in path_segments:
            curr = curr.get_directory(seg)
            if curr is None:
                return False
        return curr.has_file(filename)

    def __repr__(self):
        return f"FileSystemModel(root={self.root})"

class PathNormalizer:
    """
    Normalizes paths according to problem's rules to canonical absolute paths.
    """
    INDEX_FILE = 'index.html'

    def __init__(self, fs: FileSystemModel):
        self.fs = fs

    def normalize(self, pathname: Pathname) -> Optional[str]:
        """
        Normalize a pathname string into canonical absolute path or None if path invalid.
        Steps:
        - Split into segments
        - Resolve '.' and '..' normally but with problem rules:
          '..' parent directory accesses must not escape root.
        - Handle optional last segment index.html:
          if last segment is omitted index.html (i.e. ends with slash after directory),
          we check if index.html file exists in that directory to map equivalence.
        - Remove last slash optionally.
        Return None if path does not refer to existing web page according to problem rules.
        Return canonical absolute path string otherwise.
        """
        # We work stepwise on segments:
        segments = pathname.segments[:]
        # Defensive copy, segments are list of PathSegment
        # Use list of strings for convenience
        segs = [s.name for s in segments]

        # Check for empty root-only pathname
        if not segs:
            # path points to root directory
            # root does not contain file index.html, cannot be a web page normally
            # but if input points to '/', it can be /index.html abbreviation
            # let's check if index.html exists in root files
            if self.fs.file_exists([], self.INDEX_FILE):
                # path '/' is equivalent to /index.html
                return '/'
            else:
                return None
        
        # Build stack for canonical directory path resolution, without file name yet
        stack: List[str] = []

        # Special handling for last segment related to file or directory
        last_seg = segs[-1]

        # According to problem:
        # segments '.' and '..' are always directory names
        # We must check if last segment is a file name or directory name.

        # If last segment is a file (except if last is index.html and possible omission)
        # Let's guess by verifying fs existence.

        # In normalization we cannot just guess if last segment is file or directory.
        # According to problem - last segment can be index.html file, or ordinary file, or directory.

        # So we try two hypotheses if needed:
        # Hyp1: last segment is file
        # Hyp2: last segment is directory
        # Then we check filesystem:
        # Because index.html omission rule:
        #   /dir/index.html equals /dir/ equals /dir

        # So let's first resolve path treating last segment as file:
        parent_dirs_h1 = segs[:-1]
        possible_file = last_seg

        # resolve parent_dirs_h1 with '.', '..' treated as directory names

        canonical_parent1 = self._resolve_dirs(parent_dirs_h1)
        if canonical_parent1 is None:
            # parent directory does not exist
            # fallback to hypothesis 2: last segment is a directory
            canonical_dir2 = self._resolve_dirs(segs)
            if canonical_dir2 is None:
                # invalid path, no page
                return None
            else:
                # check if index.html exists in this directory = directory path itself is a page if index.html present
                if self.fs.file_exists(canonical_dir2, self.INDEX_FILE):
                    # directory path with possibly slash removed is valid page
                    # normalize to directory path possibly without trailing '/'
                    base_path = '/' + '/'.join(canonical_dir2)
                    # multiple ending slash removal, minimize representation for directories with index.html
                    return base_path if base_path != '' else '/'
                else:
                    # directory is not a page by itself (no index.html)
                    # so no web page exists at this path
                    return None
        else:
            # Hyp1 parent directory exists
            # check if file exists
            if self.fs.file_exists(canonical_parent1, possible_file):
                # valid file path page
                file_path = '/' + '/'.join(canonical_parent1 + [possible_file])
                # Now apply index.html omission rule if possible_file == index.html
                if possible_file == self.INDEX_FILE:
                    # this is equal to directory path with or without trailing slash
                    base_path = '/' + '/'.join(canonical_parent1)
                    # base_path == root when no parent dirs
                    base_path = base_path if base_path != '' else '/'
                    # Depending on trailing slash or not, both are equivalent.
                    # Per problem trailing slash can be omitted.
                    # Normalize final as directory path without trailing slash
                    return base_path
                else:
                    # ordinary file path no special omission
                    return file_path
            else:
                # file not exist, try Hyp2 guess: last segment is directory
                canonical_dir2 = self._resolve_dirs(segs)
                if canonical_dir2 is None:
                    return None
                else:
                    # check if directory has index.html file for page
                    if self.fs.file_exists(canonical_dir2, self.INDEX_FILE):
                        base_path = '/' + '/'.join(canonical_dir2)
                        base_path = base_path if base_path != '' else '/'
                        return base_path
                    else:
                        return None

    def _resolve_dirs(self, dirs: List[str]) -> Optional[List[str]]:
        """
        Resolve directory path considering '.' and '..' as directory names.
        They are normal directory names, but .. means parent directory.
        If 'dirs' point outside root (.. from root), returns None.
        Also verify every directory exists in fs when advancing.
        Note: '.' is a directory name representing itself, so no special collapse.
        """
        stack: List[str] = []
        for d in dirs:
            if d == '..':
                if len(stack) == 0:
                    # .. from root => invalid path
                    return None
                stack.pop()
            else:
                # '.' is normal directory name and must exist
                stack.append(d)
        # verify existence in fs
        if self.fs.directory_exists(stack):
            return stack
        else:
            return None

class WebPageRegistry:
    """
    Manages all known web pages and allows matching normalized paths to pages.
    """
    def __init__(self):
        self.page_to_id: Dict[str, int] = {}
        self.id_to_page: List[str] = []
        self.next_id = 0
    
    def add_page(self, canonical_path: str) -> int:
        """
        Add a canonical path for a page to registry.
        Returns the page id.
        """
        if canonical_path not in self.page_to_id:
            self.page_to_id[canonical_path] = self.next_id
            self.id_to_page.append(canonical_path)
            self.next_id += 1
        return self.page_to_id[canonical_path]
    
    def get_id(self, canonical_path: str) -> Optional[int]:
        """
        Get page id if exists.
        """
        return self.page_to_id.get(canonical_path)

class PathfinderAgentSoftwareModule:
    """
    Main orchestrator class for problem solution.
    Parses input, manages filesystem model, normalization, and queries answers.
    """
    def __init__(self):
        self.fs = FileSystemModel()
        self.registry = WebPageRegistry()
        self.normalizer = PathNormalizer(self.fs)

    def add_web_pages(self, pages: List[str]):
        # add pages to filesystem and registry
        for raw_path in pages:
            path = Pathname(raw_path)
            self.fs.add_path(path)

        # After all pages added, register all canonical page paths
        # For each page in given original form:
        # canonicalize paths that have no '.' or '..' (given pages guaranteed no '.' or '..')
        # And register canonical ones.

        # We do canonicalization knowing that input pages have no . or ..,
        # so normalizer will not fail, but we must carefully use normalizer

        # We register pages by their canonical normalized path:
        for raw_path in pages:
            pn = Pathname(raw_path)
            can = self.normalizer.normalize(pn)
            if can is not None:  # always should be not None for input pages
                self.registry.add_page(can)

    def query(self, p1: str, p2: str) -> str:
        """
        Given two raw pathnames strings, determine relations ("yes", "no", "not found")
        """
        pn1 = Pathname(p1)
        pn2 = Pathname(p2)
        c1 = self.normalizer.normalize(pn1)
        c2 = self.normalizer.normalize(pn2)

        if c1 is None or c2 is None:
            return "not found"
        id1 = self.registry.get_id(c1)
        id2 = self.registry.get_id(c2)
        if id1 is None or id2 is None:
            return "not found"
        return "yes" if id1 == id2 else "no"

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '0 0':
            break
        if not line:
            continue
        N, M = map(int, line.split())
        web_pages = []
        for _ in range(N):
            web_pages.append(input_lines[idx].strip())
            idx += 1
        queries_raw = []
        for _ in range(M*2):
            queries_raw.append(input_lines[idx].strip())
            idx += 1
        software = PathfinderAgentSoftwareModule()
        software.add_web_pages(web_pages)
        for q_i in range(M):
            p1 = queries_raw[2*q_i]
            p2 = queries_raw[2*q_i+1]
            ans = software.query(p1, p2)
            print(ans)

if __name__ == '__main__':
    main()