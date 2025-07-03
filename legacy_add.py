"""Adds two 4-digit numbers from input and prints the sum.

This is a Python 3.12 translation of the COBOL program OLDADD.
"""

def read_number(prompt: str = "Enter a 4-digit number: ") -> int:
    """Reads a 4-digit integer from user input."""
    value = input(prompt)
    if not (value.isdigit() and len(value) == 4):
        raise ValueError("Input must be a 4-digit number.")
    return int(value)

def add_and_display(a: int, b: int) -> None:
    """Adds two integers and prints the result as 4 digits."""
    print(f"{a + b:04d}")

def main() -> None:
    """Main entry point for the program."""
    a = read_number()
    b = read_number()
    add_and_display(a, b)

if __name__ == "__main__":
    main()
