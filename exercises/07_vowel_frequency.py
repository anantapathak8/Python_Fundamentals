"""
Exercise 07: Vowel Frequency Counter
Description: Analyzes text to compute total and individual vowel counts (A, E, I, O, U),
             calculates frequency percentages, and presents a visual distribution bar.
"""


def analyze_vowel_frequencies(text: str) -> dict[str, any]:
    """Computes occurrences of vowels, consonants, and relative frequencies."""
    vowels = "aeiou"
    vowel_counts = {v: 0 for v in vowels}
    consonant_count = 0
    other_chars_count = 0

    lowered_text = text.lower()
    for char in lowered_text:
        if char in vowel_counts:
            vowel_counts[char] += 1
        elif char.isalpha():
            consonant_count += 1
        else:
            other_chars_count += 1

    total_vowels = sum(vowel_counts.values())
    total_letters = total_vowels + consonant_count

    vowel_percentages = {}
    for v, count in vowel_counts.items():
        pct = (count / total_letters * 100.0) if total_letters > 0 else 0.0
        vowel_percentages[v] = round(pct, 2)

    return {
        "vowel_counts": vowel_counts,
        "total_vowels": total_vowels,
        "consonant_count": consonant_count,
        "other_chars_count": other_chars_count,
        "total_letters": total_letters,
        "vowel_percentages": vowel_percentages,
    }


def display_frequency_report(text: str, data: dict[str, any]) -> None:
    """Renders tabular vowel metrics with visual representation bars."""
    print("=" * 60)
    print("VOWEL FREQUENCY DISTRIBUTION")
    print("=" * 60)
    print(f"Sample Input: \"{text}\"\n")

    print(f"{'Vowel':<8}{'Count':<8}{'Share (%)':<12}{'Distribution Bar'}")
    print("-" * 60)
    for v in "aeiou":
        count = data["vowel_counts"][v]
        pct = data["vowel_percentages"][v]
        bar = "#" * count
        print(f"  {v.upper():<6}{count:<8}{pct:>5.1f}%     {bar}")

    print("-" * 60)
    print(f"Total Vowels Found   : {data['total_vowels']}")
    print(f"Total Consonants     : {data['consonant_count']}")
    print(f"Other Characters     : {data['other_chars_count']}")
    print(f"Total Letters        : {data['total_letters']}")
    print("=" * 60)


def main() -> None:
    """Interactive prompt with demo sentence fallback."""
    sample_default = "University Education empowers students across diverse disciplines."

    try:
        user_input = input("Enter a sentence to inspect (or press Enter for demo): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    chosen_text = user_input if user_input else sample_default
    if not user_input:
        print("[Notice] Using default sentence for demonstration.")

    results = analyze_vowel_frequencies(chosen_text)
    display_frequency_report(chosen_text, results)


if __name__ == "__main__":
    main()

