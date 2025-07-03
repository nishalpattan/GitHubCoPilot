def compound_interest(p: float, r: float, n: int, t: int) -> float:
    """
    Return accumulated amount using compound interest.

    Args:
        p: Principal amount.
        r: Annual interest rate (e.g., 0.05 for 5%).
        n: Number of times interest is compounded per year.
        t: Number of years.

    Returns:
        Accumulated amount after t years.
    """
    return p * (1 + r / n) ** (n * t)