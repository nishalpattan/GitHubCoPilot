def clean_text(line: str) -> str:
    """Lowercase and remove commas and periods from a line."""
    return line.lower().replace(",", "").replace(".", "")

def count_tokens(tokens: list[str], counts: dict[str, int]) -> None:
    """Update counts dict with token frequencies."""
    for tok in tokens:
        if tok in counts:
            counts[tok] += 1
        else:
            counts[tok] = 1

def process_transcript(lines: list[str]) -> dict[str, int]:
    """Return word‑count mapping for a chat transcript."""
    counts: dict[str, int] = {}
    for ln in lines:
        ln = clean_text(ln)
        tokens = ln.split()
        count_tokens(tokens, counts)
    most_common = max(counts.items(), key=lambda kv: kv[1])
    print(f"Most common word → {most_common[0]} ({most_common[1]})")
    return counts

# Sample input and function call
lines = [
  "Hello, how are you?",
  "I am fine. How are you doing?",
  "I am doing well. Thank you!"
]

# Call the function and store the result
word_counts = process_transcript(lines)

# Print the full word count dictionary
print(word_counts)
