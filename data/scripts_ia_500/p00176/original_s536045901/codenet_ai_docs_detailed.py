import math

# List of RGB color samples representing basic colors
sample1 = [
    [0, 0, 0],       # Black
    [0, 0, 255],     # Blue
    [0, 255, 0],     # Lime
    [0, 255, 255],   # Aqua
    [255, 0, 0],     # Red
    [255, 0, 255],   # Fuchsia
    [255, 255, 0],   # Yellow
    [255, 255, 255]  # White
]

# Corresponding color names for the RGB samples above
sample2 = ['black', 'blue', 'lime', 'aqua', 'red', 'fuchsia', 'yellow', 'white']

def hex_to_rgb(hex_color):
    """
    Convert a hexadecimal color string to its RGB components.

    The input hex_color should be a string starting with '#'
    followed by 6 hexadecimal characters (0-9, a-f).

    Args:
        hex_color (str): The hexadecimal color string (e.g. '#1a2b3c')

    Returns:
        tuple: A tuple (R, G, B) with integer values from 0 to 255 representing the RGB components.
    """
    # Remove the leading '#' character
    hex_digits = list(hex_color)
    hex_digits.pop(0)

    # Map hex letters to their decimal values
    hex_map = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    # Convert each character to its integer value
    for i in range(6):
        if hex_digits[i] in hex_map:
            hex_digits[i] = hex_map[hex_digits[i]]
        else:
            # Convert numeric characters directly to int
            hex_digits[i] = int(hex_digits[i])

    # Compute the decimal values for R, G, B by combining two hex digits each
    R = hex_digits[0] * 16 + hex_digits[1]
    G = hex_digits[2] * 16 + hex_digits[3]
    B = hex_digits[4] * 16 + hex_digits[5]

    return (R, G, B)

def find_closest_color(R, G, B, sample_colors, color_names):
    """
    Find the closest named color to the given RGB color.

    The distance metric used is Euclidean distance in the RGB color space.

    Args:
        R (int): Red component (0-255)
        G (int): Green component (0-255)
        B (int): Blue component (0-255)
        sample_colors (list of list of int): List of RGB samples, e.g. [[0,0,0], [255,255,255], ...]
        color_names (list of str): Corresponding color names for sample_colors

    Returns:
        str: The name of the color from color_names that is closest to the input RGB.
    """
    distances = []
    for i in range(len(sample_colors)):
        sr, sg, sb = sample_colors[i]
        # Calculate Euclidean distance between input RGB and the sample color
        dist = math.sqrt((R - sr)**2 + (G - sg)**2 + (B - sb)**2)
        distances.append(dist)
    # Find the index of the smallest distance value
    min_distance = min(distances)
    index = distances.index(min_distance)
    # Return the corresponding color name
    return color_names[index]

def main():
    """
    Main program loop which continuously reads hexadecimal color inputs from the user,
    converts them to RGB, finds the closest named color, and prints the result.

    The program terminates when the user inputs '0'.
    """
    while True:
        color_input = input()
        # Exit condition
        if color_input == '0':
            break

        # Convert hex color string to RGB tuple
        R, G, B = hex_to_rgb(color_input)

        # Find and print the closest color name
        closest_color = find_closest_color(R, G, B, sample1, sample2)
        print(closest_color)

# Run the main program loop
main()