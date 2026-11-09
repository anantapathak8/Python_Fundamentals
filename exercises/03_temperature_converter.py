"""
Exercise 03: Temperature Converter
Description: Converts temperatures across Celsius, Fahrenheit, and Kelvin scales,
             enforces physical temperature limits (absolute zero), and formats comparisons.
"""

# Physical limits in corresponding units
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_K = 0.0


def celsius_to_fahrenheit(c: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return (c * 9.0 / 5.0) + 32.0


def fahrenheit_to_celsius(f: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return (f - 32.0) * (5.0 / 9.0)


def celsius_to_kelvin(c: float) -> float:
    """Converts Celsius to Kelvin."""
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    """Converts Kelvin to Celsius."""
    return k - 273.15


def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Converts temperature between any pair of units ('C', 'F', 'K').

    Raises:
        ValueError: If temperature is below absolute zero or unit is unsupported.
    """
    from_u = from_unit.upper().strip()
    to_u = to_unit.upper().strip()

    # Absolute zero checks
    if from_u == "C" and value < ABSOLUTE_ZERO_C:
        raise ValueError(f"Temperature {value} C is below absolute zero ({ABSOLUTE_ZERO_C} C).")
    elif from_u == "F" and value < ABSOLUTE_ZERO_F:
        raise ValueError(f"Temperature {value} F is below absolute zero ({ABSOLUTE_ZERO_F} F).")
    elif from_u == "K" and value < ABSOLUTE_ZERO_K:
        raise ValueError(f"Temperature {value} K is below absolute zero (0 K).")

    if from_u == to_u:
        return value

    # Normalize source to Celsius first
    if from_u == "C":
        celsius = value
    elif from_u == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_u == "K":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown source scale: '{from_unit}'. Use C, F, or K.")

    # Convert Celsius to target scale
    if to_u == "C":
        return celsius
    elif to_u == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_u == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown destination scale: '{to_unit}'. Use C, F, or K.")


def demonstrate_all_scales(value: float, unit: str) -> None:
    """Prints a full conversion table for a given baseline temperature."""
    unit = unit.upper()
    c = convert_temperature(value, unit, "C")
    f = convert_temperature(value, unit, "F")
    k = convert_temperature(value, unit, "K")

    print("=" * 60)
    print(f"TEMPERATURE CONVERSION: {value:.2f} °{unit}")
    print("=" * 60)
    print(f"  Celsius (C)    : {c:>10.2f} °C")
    print(f"  Fahrenheit (F) : {f:>10.2f} °F")
    print(f"  Kelvin (K)     : {k:>10.2f} K")
    print("=" * 60)


def main() -> None:
    """Interactive CLI menu with demo default fallback."""
    print("Select Conversion Type:")
    print(" 1. Custom input (Value & Scale)")
    print(" 2. Run standard demo reference points (Freezing, Room, Boiling)")

    try:
        choice = input("Enter choice (1/2, default 2): ").strip()
    except (EOFError, KeyboardInterrupt):
        choice = "2"

    if choice == "1":
        try:
            val_str = input("Enter temperature numeric value: ").strip()
            unit_str = input("Enter unit scale (C, F, or K): ").strip()
            num_val = float(val_str)
            demonstrate_all_scales(num_val, unit_str)
        except ValueError as err:
            print(f"[Error] Invalid input: {err}")
    else:
        print("\n[Notice] Running standard temperature reference points:")
        reference_points = [
            (0.0, "C", "Water Freezing Point"),
            (21.0, "C", "Comfortable Room Temperature"),
            (100.0, "C", "Water Boiling Point at Sea Level"),
            (98.6, "F", "Average Human Body Temperature"),
        ]
        for val, u, desc in reference_points:
            print(f"\n--- Reference: {desc} ---")
            demonstrate_all_scales(val, u)


if __name__ == "__main__":
    main()

