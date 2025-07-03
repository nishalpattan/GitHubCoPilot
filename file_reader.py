def read_lines(path: str) -> list[str]:
    """
    Read all lines from a text file and return them stripped.

    Returns an empty list if the file is not found. Re-raises permission errors with context.

    Args:
        path: Path to the text file.

    Returns:
        List of stripped lines from the file, or an empty list if not found.
    """
    try:
        with open(path, "r") as f:
            return [ln.rstrip("\n") for ln in f]
    except FileNotFoundError:
        return []
    except PermissionError as e:
        raise PermissionError(f"Permission denied for file '{path}': {e}") from e
