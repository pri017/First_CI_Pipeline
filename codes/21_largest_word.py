"""Program 21: largest word."""

import string

def largest_word(sentence):
    """Return the first longest word, stripping surrounding punctuation."""
    largest = ""
    for word in sentence.split():
        clean = word.strip(string.punctuation)
        if len(clean) > len(largest):
            largest = clean
    return largest


if __name__ == "__main__":
    print(largest_word(input("Enter a sentence: ")))
