class Calculator:
    """Simple integer calculator."""
    def add(self, a: int, b: int) -> int:
        return a + b

    def sub(self, a: int, b: int) -> int:
        return a - b

    def mul(self, a: int, b: int) -> int:
        return a * b

    def div(self, a: int, b: int) -> float:
        return a / b  # TODO: handle divide-by-zero in tests