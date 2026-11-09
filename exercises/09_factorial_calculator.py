"""
Exercise 09: Factorial Calculator
Description: Computes factorials using both iterative and recursive implementations,
             validates domain constraints (n >= 0), and illustrates calculation expansion.
"""


def factorial_iterative(n: int) -> int:
    """Computes n! using a loop.

    Raises:
        ValueError: When n is negative.
    """
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative integers ({n}).")
    result = 1
    for factor in range(2, n + 1):
        result *= factor
    return result


def factorial_recursive(n: int) -> int:
    """Computes n! using recursion.

    Raises:
        ValueError: When n is negative.
    """
    if n < 0:
        raise ValueError(f"Factorial is not defined for negative integers ({n}).")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def get_factorial_expansion_string(n: int) -> str:
    """Returns the visual expansion of the factorial (e.g., '5 x 4 x 3 x 2 x 1')."""
    if n in (0, 1):
        return "1"
    factors = [str(i) for i in range(n, 0, -1)]
    return " x ".join(factors)


def display_factorial_report(n: int) -> None:
    """Formats and prints factorial breakdown."""
    try:
        val_iter = factorial_iterative(n)
        val_rec = factorial_recursive(n)
        expansion = get_factorial_expansion_string(n)

        print("=" * 60)
        print(f"FACTORIAL REPORT FOR n = {n}")
        print("=" * 60)
        print(f"  Formula Representation : {n}! = {expansion}")
        print(f"  Iterative Computation  : {val_iter:,}")
        print(f"  Recursive Computation  : {val_rec:,}")
        print(f"  Consistency Verification: {'MATCH' if val_iter == val_rec else 'MISMATCH'}")
        print("=" * 60)
    except ValueError as err:
        print(f"[Error] {err}")


def main() -> None:
    """Interactive loop with sample batch demo fallback."""
    try:
        user_input = input("Enter non-negative integer for factorial (or Enter for demo): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if user_input:
        try:
            n = int(user_input)
            display_factorial_report(n)
        except ValueError:
            print(f"[Error] '{user_input}' is not a valid integer.")
    else:
        print("[Notice] Running factorial demonstration on sample numbers:\n")
        sample_values = [0, 1, 5, 7, 10, 12]
        for val in sample_values:
            display_factorial_report(val)


if __name__ == "__main__":
    main()

