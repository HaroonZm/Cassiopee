import re
from collections import Counter

# Define a set of Java keywords to preserve.
JAVA_KEYWORDS = {
    'abstract', 'continue', 'for', 'new', 'switch', 'assert', 'default', 'goto', 'package',
    'synchronized', 'boolean', 'do', 'if', 'private', 'this', 'break', 'double', 'implements',
    'protected', 'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum',
    'instanceof', 'return', 'transient', 'catch', 'extends', 'int', 'short', 'try', 'char',
    'final', 'interface', 'static', 'void', 'class', 'finally', 'long', 'strictfp', 'volatile',
    'const', 'float', 'native', 'super', 'while'
}

def tokenize_code(code: str) -> list:
    """
    Tokenize the code using a regex that captures word tokens and punctuation.
    """
    tokens = re.findall(r'\w+|[^\s\w]', code)
    return tokens

def compress_token(token: str, keywords=JAVA_KEYWORDS) -> str:
    """
    Compress a token by replacing identifiers and literals with generic placeholders.
    
    - Numeric literals become 'NUM'.
    - String literals become 'STR'.
    - Character literals become 'CHR'.
    - Identifiers not in JAVA_KEYWORDS that start with lowercase become 'VAR';
      identifiers starting with uppercase (often class names) and keywords are left unchanged.
    """
    # Numeric literal.
    if re.fullmatch(r'\d+(\.\d+)?', token):
        return "NUM"
    # String literal.
    if token.startswith('"') and token.endswith('"'):
        return "STR"
    # Character literal.
    if token.startswith("'") and token.endswith("'"):
        return "CHR"
    # Identifier.
    if re.fullmatch(r'[A-Za-z_]\w*', token):
        if token in keywords:
            return token
        if token[0].isupper():
            return token
        return "VAR"
    return token

def tokenize_compressed_code(code: str) -> list:
    """
    Tokenize the code and compress tokens to remove attribute-specific information.
    """
    tokens = tokenize_code(code)
    compressed_tokens = [compress_token(token) for token in tokens]
    return compressed_tokens

def extract_compressed_nested_bigrams(code: str) -> Counter:
    """
    Extract compressed nested bigrams from the code.
    Bigrams are computed from the compressed token sequence.
    """
    tokens = tokenize_compressed_code(code)
    bigrams = zip(tokens, tokens[1:])
    bigram_list = [tuple(b) for b in bigrams]
    return Counter(bigram_list)

def extract_nested_bigrams(code: str) -> Counter:
    """
    Extract uncompressed nested bigrams from the code based on the linear token sequence.
    """
    tokens = tokenize_code(code)
    bigrams = zip(tokens, tokens[1:])
    bigram_list = [tuple(b) for b in bigrams]
    return Counter(bigram_list)
