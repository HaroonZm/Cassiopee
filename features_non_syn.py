import re

def extract_non_syntactic_features(code: str) -> dict:
    """
    Extract non-syntactic features from a code snippet.
    Features include mean line length, mean comment length, counts of spaces, tabs,
    underscores, empty lines, and common statement keywords.
    """
    features = {}
    lines = code.splitlines()
    num_lines = len(lines) if lines else 1

    # Mean line length.
    total_line_length = sum(len(line) for line in lines)
    features['mean_line_length'] = total_line_length / num_lines

    # Extract comments (single-line and block comments).
    single_line_comments = re.findall(r'//.*', code)
    block_comments = re.findall(r'/\*[\s\S]*?\*/', code)
    all_comments = single_line_comments + block_comments
    if all_comments:
        mean_comment_length = sum(len(comment) for comment in all_comments) / len(all_comments)
    else:
        mean_comment_length = 0
    features['mean_comment_length'] = mean_comment_length

    # Count spaces, tabs, underscores.
    features['num_spaces'] = code.count(' ')
    features['num_tabs'] = code.count('\t')
    features['num_underscores'] = code.count('_')

    # Count empty lines.
    features['num_empty_lines'] = sum(1 for line in lines if line.strip() == '')

    # Count common statement keywords.
    statement_keywords = ['if', 'for', 'while', 'switch', 'case', 'else', 'try', 'catch', 'finally', 'do']
    count_statements = 0
    for kw in statement_keywords:
        count_statements += len(re.findall(r'\b' + re.escape(kw) + r'\b', code))
    features['num_statement_words'] = count_statements

    return features
