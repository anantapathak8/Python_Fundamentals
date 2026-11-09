"""
Module: string_operations.py
Description: Explores string manipulation, slicing, formatting, and standard string
             methods through event registration and attendee badge generation.
"""


def clean_and_normalize_email(raw_email: str) -> str:
    """Strips whitespace, converts to lowercase, and validates basic email structure."""
    cleaned = raw_email.strip().lower()
    if "@" not in cleaned or not cleaned.endswith((".com", ".edu", ".org", ".net")):
        return f"[INVALID] {cleaned}"
    return cleaned


def generate_event_badge(full_name: str, organization: str, role: str) -> str:
    """Formats an attendee event conference badge with standard layout."""
    formatted_name = full_name.strip().title()
    formatted_org = organization.strip().upper()
    formatted_role = role.strip().capitalize()

    border = "+" + "-" * 38 + "+"
    badge = [
        border,
        f"| {'TECH FORWARD SUMMIT 2026':^36} |",
        f"| {'ATTENDEE BADGE':^36} |",
        border,
        f"| Name : {formatted_name:<29} |",
        f"| Org  : {formatted_org:<29} |",
        f"| Role : {formatted_role:<29} |",
        border,
    ]
    return "\n".join(badge)


def demonstrate_slicing_and_indexing() -> None:
    """Demonstrates positive/negative indexing and slice step operations."""
    print("=" * 60)
    print("1. String Indexing and Slicing")
    print("=" * 60)

    course_code = "PYTHON-PROG-101"
    print(f"Original string       : '{course_code}' (Length: {len(course_code)})")
    print(f"First character [0]   : '{course_code[0]}'")
    print(f"Last character [-1]   : '{course_code[-1]}'")
    print(f"Prefix slice [:6]     : '{course_code[:6]}'")
    print(f"Middle slice [7:11]   : '{course_code[7:11]}'")
    print(f"Suffix slice [-3:]    : '{course_code[-3:]}'")
    print(f"Reversed string [::-1]: '{course_code[::-1]}'")


def demonstrate_string_methods() -> None:
    """Demonstrates standard built-in string methods."""
    print("\n" + "=" * 60)
    print("2. Common String Methods")
    print("=" * 60)

    raw_text = "   python programming for data science and AI   "
    print(f"Original              : '{raw_text}'")
    print(f".strip()              : '{raw_text.strip()}'")
    print(f".upper()              : '{raw_text.upper()}'")
    print(f".title()              : '{raw_text.strip().title()}'")
    print(f".replace('python', 'Go'): '{raw_text.strip().replace('python', 'Golang')}'")

    # Splitting and joining
    skills_csv = "Python,SQL,Git,FastAPI,Docker"
    skills_list = skills_csv.split(",")
    print(f"Split CSV into list   : {skills_list}")

    joined_skills = " -> ".join(skills_list)
    print(f"Joined with arrows    : {joined_skills}")

    # Searching and counting
    sample_sentence = "Learn Python, build Python projects, love Python."
    print(f"Count of 'Python'     : {sample_sentence.count('Python')}")
    print(f"Starts with 'Learn'   : {sample_sentence.startswith('Learn')}")
    print(f"Find 'projects' index : {sample_sentence.find('projects')}")


def demonstrate_practical_formatting() -> None:
    """Demonstrates real-world email cleanup and event badge generation."""
    print("\n" + "=" * 60)
    print("3. Practical Formatting Examples")
    print("=" * 60)

    # Email cleansing demo
    raw_emails = [
        "  SARA.CONNOR@University.EDU   ",
        "john.doe@techcorp.com",
        "invalid-email-address",
    ]
    print("Cleaned Emails:")
    for email in raw_emails:
        print(f" - Before: '{email}' -> After: '{clean_and_normalize_email(email)}'")

    # Badge generation demo
    print("\nGenerated Badge:")
    badge_output = generate_event_badge("maya lin", "apex systems", "software engineer")
    print(badge_output)


def main() -> None:
    """Entry point for the script."""
    demonstrate_slicing_and_indexing()
    demonstrate_string_methods()
    demonstrate_practical_formatting()


if __name__ == "__main__":
    main()

