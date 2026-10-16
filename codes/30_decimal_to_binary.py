"""Program 30: decimal to binary."""

def decimal_to_binary(number):
    """Convert by repeated division by two, without bin()."""
    if number < 0:
        raise ValueError("The number must be non-negative")
    if number == 0:
        return "0"
    digits = []
    while number > 0:
        digits.append(str(number % 2))
        number //= 2
    return "".join(reversed(digits))


if __name__ == "__main__":
    print(decimal_to_binary(int(input("Enter a non-negative integer: "))))
