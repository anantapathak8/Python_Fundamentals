"""
Exercise 04: Number Property Classifier
Description: Classifies numeric inputs across multiple criteria: sign, parity,
             integer vs float status, and divisibility patterns.
"""


def classify_number(number: float) -> dict[str, any]:
    """Inspects a numeric value and returns its mathematical traits."""
    # Check sign
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    # Check whole number / integer parity
    is_integer = number.is_integer()
    if is_integer:
        int_val = int(number)
        parity = "Even" if int_val % 2 == 0 else "Odd"
        divisibility = {
            "by_2": int_val % 2 == 0,
            "by_3": int_val % 3 == 0,
            "by_5": int_val % 5 == 0,
            "by_10": int_val % 10 == 0,
        }
    else:
        parity = "Not applicable (fractional float)"
        divisibility = {"by_2": False, "by_3": False, "by_5": False, "by_10": False}

    # Magnitude category
    abs_val = abs(number)
    if abs_val == 0:
        magnitude = "Zero"
    elif abs_val < 10:
        magnitude = "Single-digit range (<10)"
    elif abs_val < 100:
        magnitude = "Double-digit range (10-99)"
    elif abs_val < 1000:
        magnitude = "Hundreds range (100-999)"
    else:
        magnitude = "Large (>= 1,000)"

    return {
        "value": number,
        "sign": sign,
        "is_integer": is_integer,
        "parity": parity,
        "magnitude": magnitude,
        "divisibility": divisibility,
    }


def print_classification_card(props: dict[str, any]) -> None:
    """Formats and prints a detailed classification breakdown."""
    val = props["value"]
    print("=" * 60)
    print(f"CLASSIFICATION REPORT FOR: {val}")
    print("=" * 60)
    print(f"  Sign / Polarity   : {props['sign']}")
    print(f"  Data Form         : {'Whole Integer' if props['is_integer'] else 'Floating-point'}")
    print(f"  Parity (Even/Odd) : {props['parity']}")
    print(f"  Magnitude Scale   : {props['magnitude']}")

    if props["is_integer"]:
        divs = [
            factor
            for factor, is_div in [
                ("2", props["divisibility"]["by_2"]),
                ("3", props["divisibility"]["by_3"]),
                ("5", props["divisibility"]["by_5"]),
                ("10", props["divisibility"]["by_10"]),
            ]
            if is_div
        ]
        divs_str = ", ".join(divs) if divs else "None of {2, 3, 5, 10}"
        print(f"  Divisible by      : {divs_str}")
    print("=" * 60)


def main() -> None:
    """Interactive loop with batch sample demo fallback."""
    try:
        user_input = input("Enter a number to classify (or press Enter for demo list): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if user_input:
        try:
            val = float(user_input)
            report = classify_number(val)
            print_classification_card(report)
        except ValueError:
            print(f"[Error] '{user_input}' is not a valid numeric value.")
    else:
        print("[Notice] Demonstrating with sample test numbers:\n")
        sample_numbers = [-42.0, 0.0, 15.0, 3.14159, 150.0]
        for num in sample_numbers:
            report = classify_number(num)
            print_classification_card(report)
            print()


if __name__ == "__main__":
    main()

