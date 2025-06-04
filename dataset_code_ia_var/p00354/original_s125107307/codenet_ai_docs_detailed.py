from datetime import date

def get_weekday_abbr(day: int) -> str:
    """
    Returns the abbreviated English weekday name for a given day in September 2017.
    
    Args:
        day (int): The day number in September 2017 (1 to 30).
        
    Returns:
        str: Three-letter abbreviation of the weekday ("mon", "tue", ..., "sun").
        
    Raises:
        ValueError: If the day is outside the valid range for September 2017.
    """
    # List of three-letter abbreviations for weekdays starting from Monday
    weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    
    # Create a date object for the given day in September 2017
    date_obj = date(2017, 9, day)
    
    # Get the weekday index (0=Monday, 6=Sunday)
    idx = date_obj.weekday()
    
    # Return the corresponding weekday abbreviation
    return weekdays[idx]

def main():
    """
    Main function to read input, compute the weekday abbreviation, and display the result.
    """
    # Read a day number from standard input and convert it to integer
    x = int(input("Enter a day in September 2017: "))
    
    # Get the corresponding weekday abbreviation by calling the helper function
    weekday_abbr = get_weekday_abbr(x)
    
    # Print the result to the console
    print(weekday_abbr)

# Entry point for the script
if __name__ == "__main__":
    main()