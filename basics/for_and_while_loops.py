"""
Module: for_and_while_loops.py
Description: Demonstrates for loops, while loops, range(), enumerate(), zip(),
             and loop control flow (break, continue, else) using event ticketing.
"""


def demonstrate_for_loops() -> None:
    """Demonstrates standard for loops, range, enumerate, and zip."""
    print("=" * 60)
    print("1. For Loops, Enumerate, and Zip")
    print("=" * 60)

    # Iteration with range(start, stop, step)
    print("Countdown using range(5, 0, -1):")
    for count in range(5, 0, -1):
        print(f"  T-minus {count}...")
    print("  Event doors open!")

    # Iteration with enumerate() to track indices
    speakers = ["Dr. Smith", "Elena Vance", "Raj Patel", "Carlos Mendoza"]
    print("\nConference Keynote Schedule (enumerate):")
    for index, speaker in enumerate(speakers, start=1):
        print(f"  Slot #{index}: {speaker}")

    # Iteration with zip() to combine multiple sequences
    times = ["09:00 AM", "10:30 AM", "01:00 PM", "03:00 PM"]
    rooms = ["Hall A", "Auditorium", "Hall B", "Main Stage"]
    print("\nCombined Schedule Matrix (zip):")
    for time_slot, speaker, room in zip(times, speakers, rooms):
        print(f"  [{time_slot}] {speaker:<16} in {room}")


def demonstrate_while_loops() -> None:
    """Demonstrates while loop iteration with condition checking and accumulator."""
    print("\n" + "=" * 60)
    print("2. While Loops (Processing Queue)")
    print("=" * 60)

    # Simulating event registration queue processing
    registration_queue = ["User_Alpha", "User_Beta", "User_Gamma", "User_Delta"]
    processed_count = 0

    print(f"Starting ticket queue with {len(registration_queue)} requests.")
    while registration_queue:
        current_user = registration_queue.pop(0)
        processed_count += 1
        print(f"  Processed registration for: {current_user} (Remaining: {len(registration_queue)})")

    print(f"Queue complete! Successfully registered {processed_count} attendees.")


def demonstrate_loop_control() -> None:
    """Demonstrates break, continue, and the loop-else clause."""
    print("\n" + "=" * 60)
    print("3. Loop Control Statements (break, continue, else)")
    print("=" * 60)

    attendee_badges = ["A101", "VIP-201", "INVALID", "A102", "VIP-202", "SUSPENDED", "A103"]

    print("Checking badges with 'continue' (skipping invalid badges):")
    valid_count = 0
    for badge in attendee_badges:
        if badge in ("INVALID", "SUSPENDED"):
            print(f"  [Skipped] Flagged badge detected: {badge}")
            continue
        print(f"  [Checked-In] Verified badge: {badge}")
        valid_count += 1
    print(f"Total verified check-ins: {valid_count}")

    # Searching with break and loop-else
    target_badge = "VIP-202"
    print(f"\nSearching for target badge '{target_badge}' (break & else):")
    for badge in attendee_badges:
        if badge == target_badge:
            print(f"  Found target {target_badge}! Terminating search.")
            break
    else:
        print(f"  Target badge '{target_badge}' was not located.")


def main() -> None:
    """Entry point for the script."""
    demonstrate_for_loops()
    demonstrate_while_loops()
    demonstrate_loop_control()


if __name__ == "__main__":
    main()

