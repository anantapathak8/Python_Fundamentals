"""
Exercise 10: Prime Number Checker & Generator
Description: Tests whether a number is prime using an efficient O(sqrt(n)) trial division
             algorithm, identifies divisor factors for composites, and generates prime lists.
"""

import math


def is_prime(n: int) -> tuple[bool, int | None]:
    """Tests primality of an integer n.

    Returns:
        tuple[bool, int | None]: (is_prime_flag, first_divisor_found_if_composite)
    """
    if n <= 1:
        return False, None
    if n in (2, 3):
        return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3

    # Check odd divisors up to sqrt(n)
    limit = int(math.isqrt(n))
    for divisor in range(5, limit + 1, 6):
        if n % divisor == 0:
            return False, divisor
        if n % (divisor + 2) == 0:
            return False, divisor + 2

    return True, None


def find_primes_in_range(start: int, end: int) -> list[int]:
    """Finds all prime numbers between start and end (inclusive)."""
    return [num for num in range(max(2, start), end + 1) if is_prime(num)[0]]


def display_prime_check(n: int) -> None:
    """Prints a structured verdict with mathematical justification."""
    flag, divisor = is_prime(n)

    print("=" * 60)
    print(f"PRIMALITY REPORT FOR: {n}")
    print("=" * 60)
    if flag:
        print(f"  Verdict       : PRIME NUMBER")
        print(f"  Justification : Has no divisors other than 1 and {n}.")
    else:
        print(f"  Verdict       : NOT PRIME (COMPOSITE / UNIT)")
        if n <= 1:
            print(f"  Justification : By definition, prime numbers must be integers > 1.")
        else:
            other_factor = n // divisor
            print(f"  Justification : Divisible by {divisor} ({divisor} x {other_factor} = {n}).")
    print("=" * 60)


def main() -> None:
    """Interactive loop with sample demo and prime table generation."""
    try:
        user_input = input("Enter an integer to test (or press Enter for demo): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_input = ""

    if user_input:
        try:
            val = int(user_input)
            display_prime_check(val)
        except ValueError:
            print(f"[Error] '{user_input}' is not a valid integer.")
    else:
        print("[Notice] Running demonstration on sample integers:\n")
        sample_candidates = [1, 2, 17, 21, 29, 49, 97, 100]
        for candidate in sample_candidates:
            display_prime_check(candidate)

        print("\n" + "=" * 60)
        print("ALL PRIME NUMBERS UP TO 100:")
        print("=" * 60)
        primes_to_100 = find_primes_in_range(1, 100)
        print(f"Count: {len(primes_to_100)} primes found.")
        # Print formatted in rows of 10
        for i in range(0, len(primes_to_100), 10):
            chunk = primes_to_100[i : i + 10]
            print("  ".join(f"{p:>4}" for p in chunk))
        print("=" * 60)


if __name__ == "__main__":
    main()

