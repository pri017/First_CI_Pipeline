"""Program 23: sort without sort."""

def bubble_sort(numbers):
    """Return a sorted copy using adjacent swaps, without sorting helpers."""
    result = list(numbers)
    for end in range(len(result) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if result[index] > result[index + 1]:
                result[index], result[index + 1] = result[index + 1], result[index]
                swapped = True
        if not swapped:
            break
    return result


if __name__ == "__main__":
    print(bubble_sort([int(value) for value in input("Numbers separated by spaces: ").split()]))
