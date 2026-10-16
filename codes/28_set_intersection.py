"""Program 28: set intersection."""

def set_intersection(first, second):
    """Return only the elements shared by both sets."""
    return first & second


if __name__ == "__main__":
    print(set_intersection(set(input("First set (space-separated items): ").split()), set(input("Second set: ").split())))
