def find_insertion_index(lines: list[str], search_term: str) -> int | None:
    """
    Finds the index after which we want to insert the new label.
    Returns None if search_term is not found.
    """
    for i, line in enumerate(lines):
        if search_term in line:
            return i + 1
    return None

def insert_label(lines: list[str], index: int, new_label: str) -> list[str]:
    """
    Inserts the new_label line at the specified index in the list of lines.
    Returns the modified list.
    """
    lines.insert(index, f"{new_label}\n")
    return lines