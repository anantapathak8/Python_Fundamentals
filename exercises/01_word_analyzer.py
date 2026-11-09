"""
Exercise 01: Word & Text Analyzer
Description: Analyzes user-provided text for word counts, character counts,
             unique words, vocabulary diversity, and longest/shortest words.
"""

import string


def analyze_text(text: str) -> dict[str, any]:
    """Analyzes a block of text and returns a dictionary of structural statistics.

    Args:
        text: The input string to analyze.

    Returns:
        dict containing word count, char count, unique words, longest/shortest words.
    """
    cleaned_text = text.strip()
    if not cleaned_text:
        return {
            "total_characters": 0,
            "characters_no_spaces": 0,
            "word_count": 0,
            "unique_words_count": 0,
            "longest_word": None,
            "shortest_word": None,
            "average_word_length": 0.0,
        }

    total_chars = len(cleaned_text)
    chars_no_spaces = len(cleaned_text.replace(" ", ""))

    # Normalize words by removing punctuation and converting to lowercase
    punctuation_table = str.maketrans("", "", string.punctuation)
    raw_words = cleaned_text.split()
    sanitized_words = [
        w.translate(punctuation_table).lower()
        for w in raw_words
        if w.translate(punctuation_table)
    ]

    word_count = len(sanitized_words)
    if word_count == 0:
        return {
            "total_characters": total_chars,
            "characters_no_spaces": chars_no_spaces,
            "word_count": 0,
            "unique_words_count": 0,
            "longest_word": None,
            "shortest_word": None,
            "average_word_length": 0.0,
        }

    unique_words = set(sanitized_words)
    longest = max(sanitized_words, key=len)
    shortest = min(sanitized_words, key=len)
    avg_length = round(sum(len(w) for w in sanitized_words) / word_count, 2)

    return {
        "total_characters": total_chars,
        "characters_no_spaces": chars_no_spaces,
        "word_count": word_count,
        "unique_words_count": len(unique_words),
        "longest_word": longest,
        "shortest_word": shortest,
        "average_word_length": avg_length,
    }


def display_analysis_report(text: str, stats: dict[str, any]) -> None:
    """Formats and prints the analysis report."""
    print("=" * 60)
    print("TEXT ANALYSIS REPORT")
    print("=" * 60)
    print(f"Sample Text: \"{text}\"\n")
    print(f"Total Characters (with spaces)    : {stats['total_characters']}")
    print(f"Total Characters (without spaces) : {stats['characters_no_spaces']}")
    print(f"Total Words Count                 : {stats['word_count']}")
    print(f"Unique Words Count                : {stats['unique_words_count']}")
    print(f"Longest Word                      : '{stats['longest_word']}'")
    print(f"Shortest Word                     : '{stats['shortest_word']}'")
    print(f"Average Word Length               : {stats['average_word_length']} characters")
    print("=" * 60)


def main() -> None:
    """Entry point with interactive input and fallback demo mode."""
    default_sample = "Python is a versatile, beginner-friendly programming language designed for clarity and efficiency."

    try:
        user_input = input("Enter a sentence to analyze (or press Enter for demo): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    chosen_text = user_input if user_input else default_sample
    if not user_input:
        print("[Notice] Using default sample text for demonstration.")

    results = analyze_text(chosen_text)
    display_analysis_report(chosen_text, results)


if __name__ == "__main__":
    main()

