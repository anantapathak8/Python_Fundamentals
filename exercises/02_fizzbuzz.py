"""
Exercise 02: FizzBuzz Generator
Description: Implements the classic FizzBuzz interview problem with configurable limits,
             input validation, and formatted statistical summaries.
"""


def get_fizzbuzz_value(number: int) -> str:
    """Returns 'Fizz', 'Buzz', 'FizzBuzz', or the string representation of the number."""
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


def generate_fizzbuzz_sequence(start: int = 1, end: int = 30) -> list[str]:
    """Generates the FizzBuzz sequence for the given range inclusive."""
    if start > end:
        raise ValueError("Start number cannot be greater than end number.")
    return [get_fizzbuzz_value(n) for n in range(start, end + 1)]


def display_fizzbuzz_results(start: int, end: int, sequence: list[str]) -> None:
    """Prints the FizzBuzz results and category frequencies."""
    print("=" * 60)
    print(f"FIZZBUZZ SEQUENCE ({start} to {end})")
    print("=" * 60)

    # Print in grid rows of 5
    for i in range(0, len(sequence), 5):
        chunk = sequence[i : i + 5]
        print("  ".join(f"{item:>10}" for item in chunk))

    # Frequency counts
    fizz_count = sequence.count("Fizz")
    buzz_count = sequence.count("Buzz")
    fizzbuzz_count = sequence.count("FizzBuzz")
    numeric_count = len(sequence) - (fizz_count + buzz_count + fizzbuzz_count)

    print("\n" + "-" * 60)
    print("Distribution Summary:")
    print(f"  Fizz (divisible by 3)       : {fizz_count}")
    print(f"  Buzz (divisible by 5)       : {buzz_count}")
    print(f"  FizzBuzz (divisible by 15)  : {fizzbuzz_count}")
    print(f"  Standard Numbers            : {numeric_count}")
    print("=" * 60)


def main() -> None:
    """CLI prompt with fallback demo."""
    default_end = 30

    try:
        user_input = input(f"Enter upper limit integer (default {default_end}): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if not user_input:
        print(f"[Notice] Using default limit of {default_end}.")
        end_val = default_end
    else:
        try:
            end_val = int(user_input)
            if end_val < 1:
                print("[Warning] Value must be >= 1. Defaulting to 30.")
                end_val = 30
        except ValueError:
            print("[Warning] Invalid integer input. Defaulting to 30.")
            end_val = 30

    results = generate_fizzbuzz_sequence(1, end_val)
    display_fizzbuzz_results(1, end_val, results)


if __name__ == "__main__":
    main()

