import javalang
from collections import Counter
from .discretization import discretize_bigram_features

def get_children(node):
    """
    Retrieve child nodes from an AST node by scanning its __dict__ for other nodes.
    """
    children = []
    for attr, value in node.__dict__.items():
        if isinstance(value, list):
            for item in value:
                if isinstance(item, javalang.tree.Node):
                    children.append(item)
        elif isinstance(value, javalang.tree.Node):
            children.append(value)
    return children

def extract_ast_bigrams(tree) -> Counter:
    """
    Traverse the AST recursively and extract bigrams representing parent-child relationships.
    Each bigram is a tuple of (parent_node_type, child_node_type).
    """
    bigrams = []
    def traverse(node):
        children = get_children(node)
        for child in children:
            bigrams.append((node.__class__.__name__, child.__class__.__name__))
            traverse(child)
    traverse(tree)
    return Counter(bigrams)

def extract_ast_features(code: str, bin_width: int = 3000, bigram_dict: dict = None) -> (dict, dict):
    """
    Parse the Java code into an AST, extract nested bigrams (parent-child relationships),
    discretize their frequency counts into bins, and normalize by the total number of characters.
    """
    tree = javalang.parse.parse(code)
    bigram_counts = extract_ast_bigrams(tree)
    bin_feats, bigram_dict = discretize_bigram_features(bigram_counts, bin_width=bin_width, bigram_dict=bigram_dict, s1=10)
    total_chars = len(code) if len(code) > 0 else 1
    for bin_num in bin_feats:
        bin_feats[bin_num] /= total_chars
    return bin_feats, bigram_dict
