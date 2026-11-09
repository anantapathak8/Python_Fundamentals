"""
Module: functions.py
Description: Demonstrates function definitions, positional/keyword arguments,
             default parameters, *args, **kwargs, multiple return values, and type hints.
"""


def calculate_ticket_total(
    ticket_price: float,
    quantity: int = 1,
    discount_rate: float = 0.0,
    sales_tax_rate: float = 0.08,
) -> float:
    """Calculates final ticket total including quantity, discount, and sales tax.

    Args:
        ticket_price: Base price of a single ticket.
        quantity: Number of tickets purchased (default 1).
        discount_rate: Percentage discount as decimal (e.g., 0.10 for 10%).
        sales_tax_rate: Sales tax rate as decimal (default 0.08 for 8%).

    Returns:
        Final computed total cost rounded to 2 decimal places.
    """
    subtotal = ticket_price * quantity
    discount_amount = subtotal * discount_rate
    taxable_amount = subtotal - discount_amount
    tax = taxable_amount * sales_tax_rate
    total = taxable_amount + tax
    return round(total, 2)


def get_exam_grade_and_status(score: float) -> tuple[str, bool]:
    """Determines letter grade and pass/fail status.

    Returns:
        tuple[str, bool]: (letter_grade, is_passing)
    """
    if score >= 90:
        return "A", True
    elif score >= 80:
        return "B", True
    elif score >= 70:
        return "C", True
    elif score >= 60:
        return "D", True
    else:
        return "F", False


def build_student_enrollment(
    student_id: str,
    name: str,
    *courses: str,
    department: str = "Engineering",
    **attributes: str | int | float,
) -> dict[str, any]:
    """Demonstrates combining positional args, default args, *args, and **kwargs."""
    profile = {
        "student_id": student_id,
        "name": name,
        "department": department,
        "enrolled_courses": list(courses),
        "extra_attributes": attributes,
    }
    return profile


def demonstrate_functions() -> None:
    """Demonstrates argument binding, returns, and dynamic unpackings."""
    print("=" * 60)
    print("1. Positional, Keyword, and Default Arguments")
    print("=" * 60)

    # Calling with default values
    price_single = calculate_ticket_total(100.0)
    print(f"1 Ticket @ $100 (defaults)                  : ${price_single:.2f}")

    # Calling with positional and keyword arguments
    price_group = calculate_ticket_total(100.0, 4, discount_rate=0.15)
    print(f"4 Tickets @ $100 with 15% discount (8% tax) : ${price_group:.2f}")

    print("\n" + "=" * 60)
    print("2. Multiple Return Values (Tuple Unpacking)")
    print("=" * 60)

    scores_to_check = [94.5, 78.0, 58.5]
    for score in scores_to_check:
        letter, passed = get_exam_grade_and_status(score)
        status_text = "PASSED" if passed else "FAILED"
        print(f"Score {score:>5.1f} -> Grade: {letter} | Status: {status_text}")

    print("\n" + "=" * 60)
    print("3. Arbitrary Arguments (*args and **kwargs)")
    print("=" * 60)

    student_record = build_student_enrollment(
        "ENGR-4402",
        "Jordan Miller",
        "CS101",
        "MATH201",
        "PHYS150",
        department="Computer Science",
        advisor="Prof. Vance",
        year=2,
        gpa=3.92,
    )

    print(f"Student ID : {student_record['student_id']}")
    print(f"Name       : {student_record['name']}")
    print(f"Department : {student_record['department']}")
    print(f"Courses    : {', '.join(student_record['enrolled_courses'])}")
    print(f"Attributes : {student_record['extra_attributes']}")


def main() -> None:
    """Entry point for the script."""
    demonstrate_functions()


if __name__ == "__main__":
    main()

