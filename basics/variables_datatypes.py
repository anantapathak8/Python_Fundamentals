"""
Module: variables_datatypes.py
Description: Demonstrates Python variables, primitive data types, type conversion,
             and formatted string output using a student registration scenario.
"""


def calculate_tuition(credit_hours: int, rate_per_credit: float, scholarship_discount: float) -> float:
    """Calculates the total tuition after applying scholarship discount."""
    subtotal = credit_hours * rate_per_credit
    discount_amount = subtotal * (scholarship_discount / 100.0)
    total = subtotal - discount_amount
    return total


def demonstrate_datatypes() -> None:
    """Demonstrates primary data types and dynamic typing in Python."""
    print("=" * 60)
    print("1. Primitive Data Types in Python")
    print("=" * 60)

    # String (str)
    student_name: str = "Aria Sharma"
    # Integer (int)
    student_age: int = 20
    credit_hours: int = 15
    # Float (float)
    gpa: float = 3.85
    tuition_rate: float = 350.50
    # Boolean (bool)
    is_full_time: bool = True
    has_scholarship: bool = True
    # NoneType
    dorm_room_number: str | None = None

    print(f"Student Name      : {student_name} (Type: {type(student_name).__name__})")
    print(f"Age               : {student_age} (Type: {type(student_age).__name__})")
    print(f"Credit Hours      : {credit_hours} (Type: {type(credit_hours).__name__})")
    print(f"Current GPA       : {gpa} (Type: {type(gpa).__name__})")
    print(f"Tuition Rate / Cr : ${tuition_rate:.2f} (Type: {type(tuition_rate).__name__})")
    print(f"Full-Time Status  : {is_full_time} (Type: {type(is_full_time).__name__})")
    print(f"Scholarship Award : {has_scholarship} (Type: {type(has_scholarship).__name__})")
    print(f"Dorm Room         : {dorm_room_number} (Type: {type(dorm_room_number).__name__})")


def demonstrate_type_conversion() -> None:
    """Demonstrates explicit type casting between strings, integers, floats, and booleans."""
    print("\n" + "=" * 60)
    print("2. Type Conversion (Casting)")
    print("=" * 60)

    # Parsing string to integer and float
    raw_credits_input = "18"
    raw_lab_fee_input = "125.75"

    converted_credits = int(raw_credits_input)
    converted_lab_fee = float(raw_lab_fee_input)

    print(f"String '{raw_credits_input}' converted to int  : {converted_credits} -> {type(converted_credits).__name__}")
    print(f"String '{raw_lab_fee_input}' converted to float: {converted_lab_fee} -> {type(converted_lab_fee).__name__}")

    # Numeric to string
    total_credits_str = str(converted_credits) + " Credits Enrolled"
    print(f"Concatenated string representation: {total_credits_str}")

    # Truthiness / Boolean conversion
    print(f"bool(0)     : {bool(0)} (Falsy numeric value)")
    print(f"bool(15)    : {bool(15)} (Truthy numeric value)")
    print(f"bool('')    : {bool('')} (Empty string is falsy)")
    print(f"bool('CS101'): {bool('CS101')} (Non-empty string is truthy)")


def demonstrate_practical_calculation() -> None:
    """Calculates and presents student semester fees."""
    print("\n" + "=" * 60)
    print("3. Practical Fee Calculation Demo")
    print("=" * 60)

    student_name = "Marcus Vance"
    enrolled_credits = 14
    rate_per_credit = 420.0
    discount_percentage = 15.0  # 15% academic scholarship

    final_tuition = calculate_tuition(enrolled_credits, rate_per_credit, discount_percentage)

    print(f"Student Billing Statement for: {student_name}")
    print(f"Enrolled Credits   : {enrolled_credits}")
    print(f"Rate Per Credit    : ${rate_per_credit:,.2f}")
    print(f"Subtotal Tuition   : ${enrolled_credits * rate_per_credit:,.2f}")
    print(f"Scholarship Applied: {discount_percentage}%")
    print(f"Final Amount Due   : ${final_tuition:,.2f}")


def main() -> None:
    """Entry point for the script."""
    demonstrate_datatypes()
    demonstrate_type_conversion()
    demonstrate_practical_calculation()


if __name__ == "__main__":
    main()

