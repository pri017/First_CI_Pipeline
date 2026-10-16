"""Program 22: anagram strings."""

def is_anagram(first, second):
    """Ignore case and spaces; repeated characters must match in count."""
    first = first.lower().replace(" ", "")
    second = second.lower().replace(" ", "")
    return sorted(first) == sorted(second)


if __name__ == "__main__":
    print(is_anagram(input("First string: "), input("Second string: ")))
