from .features_non_syn import extract_non_syntactic_features
from .discretization import discretize_bigram_features

def extract_features(code: str, bin_width: int = 3000, bigram_dict: dict = None, 
                     compressed: bool = False, use_ast: bool = False) -> (dict, dict):
    """
    Extract both non-syntactic features and nested bigram frequency features from the code.
    
    Options:
      - If 'compressed' is True, token-based bigrams are computed after compressing tokens.
      - If 'use_ast' is True, nested bigrams are extracted by traversing the AST (capturing parent-child relationships).
        If AST parsing fails (e.g., due to syntax errors), fallback to token-based extraction.
    
    All feature counts are normalized by the total number of characters in the code.
    
    Returns:
      - A combined feature dictionary.
      - The bigram dictionary mapping unique bigrams to indices.
    """
    total_chars = len(code) if len(code) > 0 else 1

    # Extract and normalize non-syntactic features.
    non_syn_feats = extract_non_syntactic_features(code)
    for key in non_syn_feats:
        non_syn_feats[key] /= total_chars

    if use_ast:
        # Try AST-based extraction; if it fails, fallback to token-based.
        try:
            from .features_ast import extract_ast_features
            bin_feats, bigram_dict = extract_ast_features(code, bin_width=bin_width, bigram_dict=bigram_dict)
        except Exception as e:
            print("AST parsing failed with error:", e)
            print("Falling back to token-based feature extraction.")
            if compressed:
                from .features_token import extract_compressed_nested_bigrams
                bigram_counts = extract_compressed_nested_bigrams(code)
            else:
                from .features_token import extract_nested_bigrams
                bigram_counts = extract_nested_bigrams(code)
            bin_feats, bigram_dict = discretize_bigram_features(bigram_counts, bin_width=bin_width, bigram_dict=bigram_dict, s1=10)
            for bin_num in bin_feats:
                bin_feats[bin_num] /= total_chars
    else:
        # Token-based extraction.
        if compressed:
            from .features_token import extract_compressed_nested_bigrams
            bigram_counts = extract_compressed_nested_bigrams(code)
        else:
            from .features_token import extract_nested_bigrams
            bigram_counts = extract_nested_bigrams(code)
        bin_feats, bigram_dict = discretize_bigram_features(bigram_counts, bin_width=bin_width, bigram_dict=bigram_dict, s1=10)
        for bin_num in bin_feats:
            bin_feats[bin_num] /= total_chars

    combined_features = {}
    combined_features.update(non_syn_feats)
    for bin_num, value in bin_feats.items():
        combined_features[f"nb_bin_{bin_num}"] = value

    return combined_features, bigram_dict
