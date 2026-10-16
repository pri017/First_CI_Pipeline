"""Program 27: rotate list."""

def rotate_list(items, k):
    """Return a new list rotated right; negative k rotates left."""
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k]


if __name__ == "__main__":
    print(rotate_list(input("Items separated by spaces: ").split(), int(input("Right rotation count: "))))
