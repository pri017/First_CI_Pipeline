"""Program 29: armstrong number."""

def is_armstrong(number):
    """Check whether the digit powers total the non-negative integer."""
    if number < 0:
        return False
    digits = str(number)
    total = 0
    for digit in digits:
        total += int(digit) ** len(digits)
    return total == number


if __name__ == "__main__":
    print(is_armstrong(int(input("Enter an integer: "))))
