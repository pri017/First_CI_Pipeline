"""Program 25: max min list."""

def find_max_min(numbers):
    """Return (maximum, minimum) using comparisons; reject an empty list."""
    if not numbers:
        raise ValueError("The list must not be empty")
    maximum = minimum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return maximum, minimum


if __name__ == "__main__":
    print(find_max_min([int(x) for x in input("Numbers separated by spaces: ").split()]))
