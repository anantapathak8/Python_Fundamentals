"""
Exercise 05: Palindrome Checker
Description: Evaluates whether phrases, words, or numbers read identically forwards
             and backwards, filtering punctuation, whitespaces, and case differences.
"""


def clean_text_for_palindrome(text: str) -> str:
    """Removes all non-alphanumeric characters and converts to lowercase."""
    return "".join(char.lower() for char in text if char.isalnum())


def is_palindrome(text: str) -> tuple[bool, str, str]:
    """Determines whether a text string is a palindrome.

    Returns:
        tuple[bool, str, str]: (is_palindrome_flag, cleaned_forward, reversed_string)
    """
    cleaned = clean_text_for_palindrome(text)
    reversed_str = cleaned[::-1]
    return (cleaned == reversed_str, cleaned, reversed_str)


def evaluate_and_display(phrase: str) -> None:
    """Displays side-by-side palindrome breakdown."""
    matched, cleaned, reversed_str = is_palindrome(phrase)
    status_tag = ">> PALINDROME <<" if matched else "NOT A PALINDROME"

    print("=" * 60)
    print(f"Phrase        : \"{phrase}\"")
    print(f"Sanitized     : \"{cleaned}\"")
    print(f"Reversed      : \"{reversed_str}\"")
    print(f"Result        : {status_tag}")
    print("=" * 60)


def main() -> None:
    """Interactive prompt with automated demo test suite."""
    try:
        user_input = input("Enter a word/phrase to check (or press Enter for demo suite): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if user_input:
        evaluate_and_display(user_input)
    else:
        print("[Notice] Running palindrome demo suite:\n")
        test_phrases = [
            "Racecar",
            "A man, a plan, a canal: Panama!",
            "Madam, in Eden, I'm Adam.",
            "No 'x' in Nixon",
            "Python Programming",
            "12321",
            "123456",
        ]
        for phrase in test_phrases:
            evaluate_and_display(phrase)


if __name__ == "__main__":
    main()

