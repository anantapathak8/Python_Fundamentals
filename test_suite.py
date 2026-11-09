"""
Automated Test Suite for Python Fundamentals Lab – Week 1
Verifies the functional logic and subprocess execution of all 16 Python files.
"""

import subprocess
import sys
from pathlib import Path


def test_basics_imports() -> None:
    print("Testing 'basics' package modules...")

    # 1. variables_datatypes
    from basics.variables_datatypes import calculate_tuition
    assert calculate_tuition(10, 100.0, 10.0) == 900.0
    assert calculate_tuition(0, 100.0, 0.0) == 0.0
    print("  ✓ basics/variables_datatypes.py verified.")

    # 2. string_operations
    from basics.string_operations import clean_and_normalize_email, generate_event_badge
    assert clean_and_normalize_email("  TEST@Domain.COM  ") == "test@domain.com"
    assert "[INVALID]" in clean_and_normalize_email("invalid_email")
    badge = generate_event_badge("alice smith", "acme corp", "lead developer")
    assert "Alice Smith" in badge and "ACME CORP" in badge
    print("  ✓ basics/string_operations.py verified.")

    # 3. list_operations
    from basics.list_operations import summarize_scores
    stats = summarize_scores([80.0, 90.0, 100.0])
    assert stats["count"] == 3
    assert stats["highest"] == 100.0
    assert stats["lowest"] == 80.0
    assert stats["average"] == 90.0
    print("  ✓ basics/list_operations.py verified.")

    # 4. dictionary_operations
    from basics.dictionary_operations import calculate_student_gpa
    gpa = calculate_student_gpa({"CS101": 90.0, "MATH201": 80.0})
    assert gpa == 85.0
    print("  ✓ basics/dictionary_operations.py verified.")

    # 5. for_and_while_loops
    # Verify module imports and functions run
    import basics.for_and_while_loops
    print("  ✓ basics/for_and_while_loops.py verified.")

    # 6. functions
    from basics.functions import calculate_ticket_total, get_exam_grade_and_status, build_student_enrollment
    assert calculate_ticket_total(100.0, 1, 0.0, 0.08) == 108.0
    grade, status = get_exam_grade_and_status(95.0)
    assert grade == "A" and status is True
    record = build_student_enrollment("S1", "Test User", "C1", "C2", role="Student")
    assert record["student_id"] == "S1"
    assert len(record["enrolled_courses"]) == 2
    print("  ✓ basics/functions.py verified.")


def test_exercises_logic() -> None:
    print("\nTesting 'exercises' modules logic...")

    # Exercise 01
    from exercises import (
        _01_mod,
        _02_mod,
        _03_mod,
        _04_mod,
        _05_mod,
        _06_mod,
        _07_mod,
        _08_mod,
        _09_mod,
        _10_mod,
    )

    # 01 Word analyzer
    res1 = _01_mod.analyze_text("Hello world! Hello Python.")
    assert res1["word_count"] == 4
    assert res1["unique_words_count"] == 3
    print("  ✓ exercises/01_word_analyzer.py verified.")

    # 02 Fizzbuzz
    assert _02_mod.get_fizzbuzz_value(3) == "Fizz"
    assert _02_mod.get_fizzbuzz_value(5) == "Buzz"
    assert _02_mod.get_fizzbuzz_value(15) == "FizzBuzz"
    assert _02_mod.get_fizzbuzz_value(7) == "7"
    print("  ✓ exercises/02_fizzbuzz.py verified.")

    # 03 Temperature converter
    assert abs(_03_mod.celsius_to_fahrenheit(0.0) - 32.0) < 0.001
    assert abs(_03_mod.fahrenheit_to_celsius(32.0) - 0.0) < 0.001
    assert abs(_03_mod.celsius_to_kelvin(0.0) - 273.15) < 0.001
    print("  ✓ exercises/03_temperature_converter.py verified.")

    # 04 Number classifier
    c_pos = _04_mod.classify_number(42.0)
    assert c_pos["sign"] == "Positive"
    assert c_pos["parity"] == "Even"
    assert c_pos["is_integer"] is True
    c_neg = _04_mod.classify_number(-7.5)
    assert c_neg["sign"] == "Negative"
    assert c_neg["is_integer"] is False
    print("  ✓ exercises/04_number_classifier.py verified.")

    # 05 Palindrome checker
    assert _05_mod.is_palindrome("racecar")[0] is True
    assert _05_mod.is_palindrome("A man, a plan, a canal: Panama!")[0] is True
    assert _05_mod.is_palindrome("Python")[0] is False
    print("  ✓ exercises/05_palindrome_checker.py verified.")

    # 06 Basic calculator
    assert _06_mod.calculate(10, "+", 5) == 15
    assert _06_mod.calculate(10, "-", 4) == 6
    assert _06_mod.calculate(10, "*", 3) == 30
    assert _06_mod.calculate(10, "/", 2) == 5.0
    assert _06_mod.calculate(2, "**", 3) == 8
    try:
        _06_mod.calculate(5, "/", 0)
        assert False, "ZeroDivisionError expected"
    except ZeroDivisionError:
        pass
    print("  ✓ exercises/06_basic_calculator.py verified.")

    # 07 Vowel frequency
    vf = _07_mod.analyze_vowel_frequencies("Apple")
    assert vf["vowel_counts"]["a"] == 1
    assert vf["vowel_counts"]["e"] == 1
    assert vf["total_vowels"] == 2
    print("  ✓ exercises/07_vowel_frequency.py verified.")

    # 08 Number guessing logic
    assert _08_mod.evaluate_guess(10, 50) == "TOO_LOW"
    assert _08_mod.evaluate_guess(80, 50) == "TOO_HIGH"
    assert _08_mod.evaluate_guess(50, 50) == "CORRECT"
    print("  ✓ exercises/08_number_guessing.py verified.")

    # 09 Factorial calculator
    assert _09_mod.factorial_iterative(0) == 1
    assert _09_mod.factorial_iterative(5) == 120
    assert _09_mod.factorial_recursive(5) == 120
    assert _09_mod.factorial_recursive(6) == 720
    print("  ✓ exercises/09_factorial_calculator.py verified.")

    # 10 Prime checker
    assert _10_mod.is_prime(2)[0] is True
    assert _10_mod.is_prime(17)[0] is True
    assert _10_mod.is_prime(1)[0] is False
    assert _10_mod.is_prime(4)[0] is False
    assert _10_mod.find_primes_in_range(1, 10) == [2, 3, 5, 7]
    print("  ✓ exercises/10_prime_number_checker.py verified.")


def test_subprocess_executions() -> None:
    print("\nTesting standalone execution of all 16 files via subprocess...")
    python_exe = sys.executable

    files_to_run = [
        "basics/variables_datatypes.py",
        "basics/string_operations.py",
        "basics/list_operations.py",
        "basics/dictionary_operations.py",
        "basics/for_and_while_loops.py",
        "basics/functions.py",
        "exercises/01_word_analyzer.py",
        "exercises/02_fizzbuzz.py",
        "exercises/03_temperature_converter.py",
        "exercises/04_number_classifier.py",
        "exercises/05_palindrome_checker.py",
        "exercises/06_basic_calculator.py",
        "exercises/07_vowel_frequency.py",
        "exercises/08_number_guessing.py",
        "exercises/09_factorial_calculator.py",
        "exercises/10_prime_number_checker.py",
    ]

    for rel_path in files_to_run:
        full_path = Path(__file__).parent / rel_path
        proc = subprocess.run(
            [python_exe, str(full_path)],
            input="\n\n\n",
            capture_output=True,
            text=True,
            timeout=10,
        )
        if proc.returncode != 0:
            print(f"FAILED: {rel_path}\nStderr:\n{proc.stderr}")
            sys.exit(1)
        else:
            print(f"  ✓ Process Exit 0: {rel_path}")


if __name__ == "__main__":
    # Create dynamic module aliases for exercises since their filenames start with numbers
    import importlib.util

    class ExercisesLoader:
        pass

    ex_loader = ExercisesLoader()
    base_dir = Path(__file__).parent / "exercises"
    for i in range(1, 11):
        filename_prefix = f"{i:02d}_"
        matching_file = next(base_dir.glob(f"{filename_prefix}*.py"))
        spec = importlib.util.spec_from_file_location(f"ex_{i}", matching_file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        setattr(ex_loader, f"_{i:02d}_mod", mod)

    sys.modules["exercises"] = ex_loader

    test_basics_imports()
    test_exercises_logic()
    test_subprocess_executions()
    print("\n" + "=" * 60)
    print("ALL 16 PYTHON PROGRAMS AND TESTS PASSED SUCCESSFULLY!")
    print("=" * 60)

