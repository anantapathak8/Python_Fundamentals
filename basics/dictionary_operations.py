"""
Module: dictionary_operations.py
Description: Explores Python dictionaries, key-value mapping, safe retrieval,
             nested structures, and comprehensions through a student gradebook system.
"""


def calculate_student_gpa(courses: dict[str, float]) -> float:
    """Calculates average score across enrolled courses."""
    if not courses:
        return 0.0
    total = sum(courses.values())
    return round(total / len(courses), 2)


def demonstrate_dictionary_basics() -> None:
    """Demonstrates creation, access, modification, and safe lookups."""
    print("=" * 60)
    print("1. Dictionary Basics & Lookups")
    print("=" * 60)

    # Initializing a student profile dictionary
    student = {
        "id": "STU-1001",
        "name": "Maya Patel",
        "major": "Computer Science",
        "credits": 45,
    }
    print(f"Initial Student Profile: {student}")

    # Accessing existing keys
    print(f"Student Name (bracket) : {student['name']}")

    # Safe access using .get() with fallback
    advisor = student.get("advisor", "Not Yet Assigned")
    print(f"Advisor (.get default) : {advisor}")

    # Adding new key-value pair and updating existing
    student["advisor"] = "Dr. Richardson"
    student["credits"] += 15  # completed another semester
    print(f"Updated Profile        : {student}")

    # Removing a key using pop()
    removed_major = student.pop("major")
    print(f"Removed Major          : {removed_major}")
    print(f"Profile After pop()    : {student}")


def demonstrate_iteration_and_membership() -> None:
    """Demonstrates keys, values, items, and membership checks."""
    print("\n" + "=" * 60)
    print("2. Iteration and Membership")
    print("=" * 60)

    course_enrollment = {
        "CS101": 120,
        "MATH201": 85,
        "ENG102": 95,
        "PHY150": 60,
    }

    # Checking key existence
    print(f"Is 'CS101' offered?    : {'CS101' in course_enrollment}")
    print(f"Is 'BIO101' offered?   : {'BIO101' in course_enrollment}")

    # Iterating over items
    print("\nCourse Enrollment Breakdown:")
    for code, seat_count in course_enrollment.items():
        print(f" - {code:<8}: {seat_count} students registered")

    # Dictionary comprehension: courses with high capacity (> 80 seats)
    large_courses = {k: v for k, v in course_enrollment.items() if v > 80}
    print(f"\nLarge Classes (>80)    : {large_courses}")


def demonstrate_nested_structures() -> None:
    """Demonstrates nested dictionaries using a comprehensive university gradebook."""
    print("\n" + "=" * 60)
    print("3. Nested Dictionaries (Gradebook Example)")
    print("=" * 60)

    gradebook: dict[str, dict[str, any]] = {
        "STU-201": {
            "name": "Liam Connor",
            "courses": {"CS101": 92.0, "MATH201": 88.5, "HIST100": 95.0},
        },
        "STU-202": {
            "name": "Sophia Zhang",
            "courses": {"CS101": 84.0, "MATH201": 79.0, "PHY150": 91.0},
        },
    }

    # Displaying student grade summaries
    for student_id, data in gradebook.items():
        name = data["name"]
        courses = data["courses"]
        average = calculate_student_gpa(courses)
        print(f"Student: {name} (ID: {student_id})")
        for subject, score in courses.items():
            print(f"   {subject:<8}: {score}")
        print(f"   Average Score: {average:.2f}\n")


def main() -> None:
    """Entry point for the script."""
    demonstrate_dictionary_basics()
    demonstrate_iteration_and_membership()
    demonstrate_nested_structures()


if __name__ == "__main__":
    main()

