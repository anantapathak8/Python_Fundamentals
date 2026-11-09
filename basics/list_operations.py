"""
Module: list_operations.py
Description: Demonstrates list manipulation, slicing, mutation, sorting,
             comprehensions, and aggregations using a workshop registration scenario.
"""


def summarize_scores(scores: list[float]) -> dict[str, float]:
    """Calculates summary statistics (count, highest, lowest, average) for scores."""
    if not scores:
        return {"count": 0, "highest": 0.0, "lowest": 0.0, "average": 0.0}

    total = sum(scores)
    count = len(scores)
    highest = max(scores)
    lowest = min(scores)
    average = round(total / count, 2)

    return {
        "count": count,
        "highest": highest,
        "lowest": lowest,
        "average": average,
    }


def demonstrate_list_basics() -> None:
    """Shows list creation, indexing, slicing, and mutation."""
    print("=" * 60)
    print("1. List Basics & Modification")
    print("=" * 60)

    attendees = ["Alice", "Bob", "Charlie", "Diana"]
    print(f"Initial Attendees      : {attendees}")

    # Appending a single attendee
    attendees.append("Ethan")
    print(f"After append('Ethan')  : {attendees}")

    # Inserting at specific position
    attendees.insert(1, "Bella")
    print(f"After insert(1, 'Bella'): {attendees}")

    # Extending with another batch
    late_arrivals = ["Fiona", "George"]
    attendees.extend(late_arrivals)
    print(f"After extend()         : {attendees}")

    # Removing by value
    attendees.remove("Charlie")
    print(f"After remove('Charlie'): {attendees}")

    # Popping last attendee
    last_removed = attendees.pop()
    print(f"After pop() ('{last_removed}') : {attendees}")

    # Slicing
    first_three = attendees[:3]
    print(f"First 3 attendees      : {first_three}")


def demonstrate_sorting_and_searching() -> None:
    """Demonstrates search checks, sorting in-place vs sorted copy, and reversing."""
    print("\n" + "=" * 60)
    print("2. Searching, Sorting, and Reversing")
    print("=" * 60)

    scores = [88.5, 92.0, 79.5, 95.0, 84.0, 91.5]
    print(f"Original Scores        : {scores}")

    # Checking membership
    target_score = 92.0
    is_present = target_score in scores
    print(f"Is {target_score} in scores?   : {is_present}")

    # Non-destructive sorting using sorted()
    ascending_scores = sorted(scores)
    print(f"Sorted (new list)      : {ascending_scores}")
    print(f"Original untouched     : {scores}")

    # In-place sorting in descending order
    scores.sort(reverse=True)
    print(f"In-place sorted (desc) : {scores}")

    # Reversing in-place
    scores.reverse()
    print(f"Reversed in-place      : {scores}")


def demonstrate_comprehensions_and_stats() -> None:
    """Demonstrates list comprehensions and real-world summary calculations."""
    print("\n" + "=" * 60)
    print("3. List Comprehensions & Practical Analytics")
    print("=" * 60)

    raw_scores = [68.0, 74.5, 82.0, 91.5, 59.0, 88.0, 94.0]
    print(f"Raw Class Scores       : {raw_scores}")

    # Filtering passing scores (>= 70) with a list comprehension
    passing_scores = [score for score in raw_scores if score >= 70.0]
    print(f"Passing Scores (>=70)  : {passing_scores}")

    # Applying curve (+5 points capped at 100) with comprehension
    curved_scores = [min(score + 5.0, 100.0) for score in raw_scores]
    print(f"Curved Scores (+5 max 100): {curved_scores}")

    # Statistical summary
    stats = summarize_scores(curved_scores)
    print("\nCurved Exam Summary:")
    print(f" - Student Count : {int(stats['count'])}")
    print(f" - Highest Score : {stats['highest']}")
    print(f" - Lowest Score  : {stats['lowest']}")
    print(f" - Class Average : {stats['average']}")


def main() -> None:
    """Entry point for the script."""
    demonstrate_list_basics()
    demonstrate_sorting_and_searching()
    demonstrate_comprehensions_and_stats()


if __name__ == "__main__":
    main()

