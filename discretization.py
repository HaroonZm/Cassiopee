from collections import defaultdict

def discretize_bigram_features(bigram_counts, bin_width: int = 3000, bigram_dict: dict = None, s1: int = 10) -> (dict, dict):
    """
    Map each unique bigram to a unique index (starting at s1) and aggregate frequency counts into bins.
    The bin number is computed as: bin_num = (index - s1) // bin_width.
    """
    if bigram_dict is None:
        bigram_dict = {}
    for bigram in bigram_counts:
        if bigram not in bigram_dict:
            bigram_dict[bigram] = len(bigram_dict) + s1

    bin_features = defaultdict(int)
    for bigram, count in bigram_counts.items():
        idx = bigram_dict[bigram]
        bin_num = (idx - s1) // bin_width
        bin_features[bin_num] += count
    return dict(bin_features), bigram_dict
