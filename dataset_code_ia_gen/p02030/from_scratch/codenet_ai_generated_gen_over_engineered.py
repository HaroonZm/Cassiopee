class PostingList:
    def __init__(self, postings):
        self._postings = postings
        self._index = {doc_id: True for doc_id in postings}  # For O(1) membership tests
        
    @classmethod
    def from_input(cls, n, postings_str):
        postings = list(map(int, postings_str.split()))
        assert len(postings) == n
        # Enforce sorted constraint (might be used later)
        assert all(postings[i] < postings[i+1] for i in range(len(postings)-1))
        return cls(postings)
    
    def __len__(self):
        return len(self._postings)
    
    def intersect(self, other: "PostingList") -> "PostingList":
        # Anticipating optimized intersection for varying data types or huge data
        return PostingList._intersect_sorted_lists(self._postings, other._postings)
        
    def union(self, other: "PostingList") -> "PostingList":
        # Anticipating optimized union for large sorted lists possibly with duplicates
        return PostingList._union_sorted_lists(self._postings, other._postings)
        
    @staticmethod
    def _intersect_sorted_lists(a, b):
        # Two pointers intersection for sorted arrays
        i, j = 0, 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return PostingList(result)
    
    @staticmethod
    def _union_sorted_lists(a, b):
        # Two pointers union for sorted arrays
        i, j = 0, 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        # Append remainder
        if i < len(a):
            result.extend(a[i:])
        if j < len(b):
            result.extend(b[j:])
        return PostingList(result)
    
    def ids(self):
        # Return the internal sorted list
        return self._postings


class SearchEngine:
    def __init__(self):
        self._posting_lists = dict()
        
    def add_posting_list(self, key: str, posting_list: PostingList):
        self._posting_lists[key] = posting_list
    
    def and_search(self, key1: str, key2: str) -> PostingList:
        p1 = self._posting_lists[key1]
        p2 = self._posting_lists[key2]
        return p1.intersect(p2)
    
    def or_search(self, key1: str, key2: str) -> PostingList:
        p1 = self._posting_lists[key1]
        p2 = self._posting_lists[key2]
        return p1.union(p2)


class AndOrSearchApp:
    def __init__(self):
        self.engine = SearchEngine()
    
    def run(self):
        # Read first line: sizes
        n, m = map(int, input().split())
        a_line = input()
        b_line = input()
        # Initialize PostingList with strict checks and encapsulation
        a_posting = PostingList.from_input(n, a_line)
        b_posting = PostingList.from_input(m, b_line)
        
        self.engine.add_posting_list("A", a_posting)
        self.engine.add_posting_list("B", b_posting)
        
        and_result = self.engine.and_search("A", "B")
        or_result = self.engine.or_search("A", "B")
        
        # Output format
        print(len(and_result), len(or_result))
        for doc_id in and_result.ids():
            print(doc_id)
        for doc_id in or_result.ids():
            print(doc_id)


if __name__ == "__main__":
    AndOrSearchApp().run()