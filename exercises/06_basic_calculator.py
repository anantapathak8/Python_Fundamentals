"""
Exercise 06: Basic Arithmetic Calculator
Description: Performs basic mathematical operations (+, -, *, /, //, %, **),
             validates inputs, and handles zero division and parsing exceptions safely.
"""


def calculate(first_num: float, operator: str, second_num: float) -> float:
    """Executes the calculation based on the provided operator.

    Raises:
        ZeroDivisionError: When dividing or modulating by zero.
        ValueError: For unsupported mathematical operators.
    """
    op = operator.strip()

    if op == "+":
        return first_num + second_num
    elif op == "-":
        return first_num - second_num
    elif op == "*":
        return first_num * second_num
    elif op == "/":
        if second_num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_num / second_num
    elif op == "//":
        if second_num == 0:
            raise ZeroDivisionError("Cannot floor divide by zero.")
        return first_num // second_num
    elif op == "%":
        if second_num == 0:
            raise ZeroDivisionError("Cannot compute modulo with zero divisor.")
        return first_num % second_num
    elif op in ("**", "^"):
        return first_num ** second_num
    else:
        raise ValueError(f"Unsupported operator '{operator}'. Choose from +, -, *, /, //, %, **")


def run_single_calculation(a_str: str, op_str: str, b_str: str) -> None:
    """Parses and computes a single arithmetic expression with error feedback."""
    try:
        a = float(a_str)
        b = float(b_str)
        result = calculate(a, op_str, b)
        # Format as integer if it represents a whole number
        res_display = int(result) if result.is_integer() else f"{result:.4f}".rstrip("0")
        print(f"Result: {a} {op_str} {b} = {res_display}")
    except ValueError as val_err:
        print(f"[Input Error] {val_err}")
    except ZeroDivisionError as zero_err:
        print(f"[Math Error] {zero_err}")


def main() -> None:
    """Interactive loop with fallback demo if inputs are absent."""
    print("=" * 60)
    print("PYTHON ARITHMETIC CALCULATOR")
    print("Supported Operators: +  -  *  /  //  %  **")
    print("=" * 60)

    try:
        user_a = input("Enter first number (or Enter for demo suite): ").strip()
    except (EOFError, KeyboardInterrupt):
        user_a = ""

    if user_a:
        try:
            user_op = input("Enter operator (+, -, *, /, //, %, **): ").strip()
            user_b = input("Enter second number: ").strip()
            run_single_calculation(user_a, user_op, user_b)
        except (EOFError, KeyboardInterrupt):
            print("\nOperation cancelled.")
    else:
        print("[Notice] Running automated calculator demo suite:\n")
        demo_cases = [
            ("25", "+", "17"),
            ("100", "-", "42.5"),
            ("12.5", "*", "4"),
            ("144", "/", "12"),
            ("17", "//", "5"),
            ("17", "%", "5"),
            ("2", "**", "8"),
            ("10", "/", "0"),   # Demonstrates ZeroDivisionError handling
            ("15", "@", "3"),   # Demonstrates invalid operator handling
        ]
        for a, op, b in demo_cases:
            print(f"Expression: {a} {op} {b}")
            run_single_calculation(a, op, b)
            print("-" * 40)


if __name__ == "__main__":
    main()

