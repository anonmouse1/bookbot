def count_words(booktext):
    num_words = booktext.split()
    count = len(num_words)
    #print(f"Found {count} total words")
    return count

def char_count(text: str) -> dict:
    """
    Count each character (case-insensitive) in the given text.
    Returns a dictionary with characters as keys and counts as values.
    """
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_counts(counts: dict) -> list:
    """
    Take a dict of character counts and return a list of
    {"char": <character>, "num": <count>} dicts sorted by count, descending.
    """
    # Build list of dictionaries from the counts dict
    result = []
    for ch, num in counts.items():
        result.append({"char": ch, "num": num})

    # Helper function for .sort key
    def get_num(item: dict) -> int:
        return item["num"]

    # Sort in-place from greatest to least
    result.sort(key=get_num, reverse=True)
    return result

