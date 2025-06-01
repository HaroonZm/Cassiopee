def work(item):
    """
    Calculate the minimum cost to produce a given item.

    This function recursively computes the cost of an item by comparing
    its direct price with the total cost of producing it from its recipe components.
    It updates the global price list with the minimum cost once calculated
    and removes the recipe to avoid recalculations.

    Args:
        item (str): The name of the item to calculate the cost for.

    Returns:
        int: The minimum price to produce the item.
    """
    # Check if the item has a recipe defined
    if recipe.has_key(item):
        price = 0
        # Sum the minimum cost of each component in the recipe
        for i in recipe[item]:
            price += work(i)
        # Update the price list with the minimum of current price and recipe cost
        p_list[item] = min(price, p_list[item])
        # Remove the recipe once processed to optimize future lookups
        del recipe[item]
    # Return the minimum price found for the item
    return p_list[item]

while True:
    # Initialize price list and recipe dictionary for each test case
    p_list = {}
    recipe = {}

    # Read the number of items with fixed prices
    n = input()
    # Exit loop if n is 0 (end of input)
    if n == 0:
        break

    # Read each item and its direct price, store in p_list
    for i in range(n):
        item, price = raw_input().split()
        p_list[item] = int(price)

    # Read the number of recipes
    m = input()
    # For each recipe, read its details and populate recipe dictionary
    for i in range(m):
        data = raw_input().split()
        # The first element is the item name
        recipe[data[0]] = []
        # Number of components in the recipe is the second element
        component_count = int(data[1])
        # Append each component to the recipe list for the item
        for j in range(component_count):
            recipe[data[0]].append(data[j + 2])

    # If there are no recipes, directly print the price of the queried item
    if m == 0:
        print p_list[raw_input()]
    else:
        # Otherwise, read the target item and compute its minimum cost
        price = work(raw_input())
        print price