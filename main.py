from .utils import split_into_groups
from .features import extract_features

def main():
    # Update the file path as needed.
    file_path = "GPT-Java-GCJ-Dataset-main/dataset/__jordanu_000000000019fd27_000000000022a4f7_000000000020993c.java"
    with open(file_path, "r") as f:
        content = f.read()
    
    groups = split_into_groups(content, group_size=40)
    print("Number of groups:", len(groups))
    
    # For demonstration, process the first group.
    sample_code = content[:3000]
    # Set use_ast=True to use the AST-based method (structural features)
    # and compressed=True to use token-based compression if use_ast were False.
    features, bigram_dict = extract_features(sample_code, bin_width=3000, compressed=True, use_ast=True)
    
    print("\nExtracted Features:")
    for key, value in features.items():
        print(f"{key}: {value:.4f}")
    
    print("\nBigram Dictionary (sample):")
    # Print only the first 10 entries for brevity.
    for i, (bigram, idx) in enumerate(bigram_dict.items()):
        if i >= 10:
            break
        print(f"{bigram}: {idx}")

if __name__ == "__main__":
    main()
