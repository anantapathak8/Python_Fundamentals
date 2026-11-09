"""
Exercise 08: Number Guessing Game
Description: Interactive number guessing game with bounds validation, attempt tracking,
             directional hints, and an automated binary search simulation mode.
"""

import random


def evaluate_guess(guess: int, secret: int) -> str:
    """Compares user guess against the secret number."""
    if guess < secret:
        return "TOO_LOW"
    elif guess > secret:
        return "TOO_HIGH"
    else:
        return "CORRECT"


def simulate_ai_game(lower: int = 1, upper: int = 100, secret: int | None = None) -> None:
    """Demonstrates game mechanics using an optimal binary search player."""
    if secret is None:
        secret = random.randint(lower, upper)

    print("=" * 60)
    print(f"AUTOMATED SIMULATION MODE (Range: {lower} - {upper})")
    print(f"[Internal] Secret Target Selected: {secret}")
    print("=" * 60)

    low = lower
    high = upper
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2
        verdict = evaluate_guess(guess, secret)

        if verdict == "CORRECT":
            print(f"Attempt #{attempts}: Guessed {guess} -> Target Hit! Won in {attempts} tries.")
            break
        elif verdict == "TOO_LOW":
            print(f"Attempt #{attempts}: Guessed {guess} -> Too Low! Searching higher...")
            low = guess + 1
        else:
            print(f"Attempt #{attempts}: Guessed {guess} -> Too High! Searching lower...")
            high = guess - 1

    print("=" * 60)


def play_interactive_game(lower: int = 1, upper: int = 100, max_attempts: int = 7) -> None:
    """Runs a human-player interactive session with validation and attempt limit."""
    secret = random.randint(lower, upper)
    attempts = 0

    print("=" * 60)
    print(f"WELCOME TO THE NUMBER GUESSING GAME!")
    print(f"I'm thinking of a number between {lower} and {upper}.")
    print(f"You have {max_attempts} attempts. Good luck!")
    print("=" * 60)

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        prompt = f"\n[Attempt {attempts}/{max_attempts}] Enter guess ({lower}-{upper}): "

        try:
            raw_input = input(prompt).strip()
            guess = int(raw_input)
        except ValueError:
            print("[Invalid] Please enter a valid integer.")
            attempts -= 1  # Do not penalize for bad format
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nGame aborted by user.")
            return

        if guess < lower or guess > upper:
            print(f"[Out of Bounds] Please stay within {lower} and {upper}.")
            attempts -= 1
            continue

        verdict = evaluate_guess(guess, secret)
        if verdict == "CORRECT":
            print(f"\nCONGRATULATIONS! You guessed {secret} correctly in {attempts} attempt(s)!")
            return
        elif verdict == "TOO_LOW":
            print(f"Too low! Try a higher number.")
        else:
            print(f"Too high! Try a lower number.")

    print(f"\nGame Over! You have exhausted all {max_attempts} attempts.")
    print(f"The secret number was: {secret}")


def main() -> None:
    """Prompt user to choose between Interactive Mode and AI Simulation Demo."""
    print("Select Mode:")
    print(" 1. Interactive Play")
    print(" 2. Watch Binary Search AI Demo")

    try:
        choice = input("Enter choice (1/2, default 2): ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = "2"

    if choice == "1":
        play_interactive_game()
    else:
        print("[Notice] Running Automated Binary Search Simulation:")
        simulate_ai_game(1, 100)


if __name__ == "__main__":
    main()

