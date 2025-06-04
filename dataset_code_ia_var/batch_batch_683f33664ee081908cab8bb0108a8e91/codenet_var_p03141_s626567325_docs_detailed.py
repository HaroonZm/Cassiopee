def calculate_takahashi_happiness():
    """
    Reads input for number of dishes and the happiness scores for Takahashi and Aoki for each dish.
    Calculates the total advantage in happiness that Takahashi can achieve by alternating turns choosing dishes,
    assuming both play optimally. Outputs the final result.
    """

    # Read the number of dishes
    n = int(input())
    # c will store the total happiness (sum of Takahashi's and Aoki's happiness) for each dish
    c = []
    # bs will accumulate the total happiness Aoki would earn if he consumes all dishes
    bs = 0

    # Iterate through each dish
    for i in range(n):
        # Read Takahashi's and Aoki's happiness values for the i-th dish
        a, b = map(int, input().split())
        # Add Aoki's happiness for this dish to the total
        bs += b
        # Store the combined happiness for this dish
        c.append(a + b)

    # Sort the combined happiness values in descending order so that higher-valued dishes are prioritized
    c.sort()
    c.reverse()

    # Initialize the answer. Start with negative Aoki's total potential happiness.
    ans = -bs
    # Takahashi and Aoki will choose dishes in turns; Takahashi goes first, picks all even indices
    for i in range(n):
        if i % 2 == 0:  # Takahashi's turn (even indices, 0-based)
            ans += c[i]  # Add the total combined happiness for this dish

    # Print the final winning margin for Takahashi
    print(ans)