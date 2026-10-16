"""Program 26: sum of list."""

def sum_of_list(numbers):
    """Accumulate the elements with a loop; an empty list totals zero."""
    total = 0
    for number in numbers:
        total += number
    return total


if __name__ == "__main__":
    print(sum_of_list([int(x) for x in input("Numbers separated by spaces: ").split()]))
