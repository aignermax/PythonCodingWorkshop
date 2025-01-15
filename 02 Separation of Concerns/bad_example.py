def parse_and_insert_label(file_path, search_term, new_label):
    """
    BAD EXAMPLE:
    1) Reads the file lines.
    2) Searches for a specific position (based on search_term).
    3) Inserts the new_label at that position.
    4) Writes the updated lines back.
    5) Prints logs directly (UI).
    All in a single function -> violates Separation of Concerns.
    """
    print("Opening file...")
    with open(file_path, "r") as f:
        lines = f.readlines()
    
    insertion_index = None
    for i, line in enumerate(lines):
        if search_term in line:
            insertion_index = i + 1
            break

    if insertion_index is None:
        print(f"Search term '{search_term}' not found. No label inserted.")
        return

    # Insert the new label line right after the search_term
    lines.insert(insertion_index, f"{new_label}\n")

    print("Writing changes to file...")
    with open(file_path, "w") as f:
        f.writelines(lines)

    print(f"Label '{new_label}' successfully inserted after '{search_term}' in {file_path}!")

# Demonstration
if __name__ == "__main__":
    # Example usage
    parse_and_insert_label(
        file_path="cad_savefile.txt",
        search_term="#INSERT_LABEL_HERE",
        new_label="#NEW_LABEL: MyCustomLabel"
    )








# Problems with bad_example.py
# Single Responsibility Principle violation: One function handles:
# File reading and writing
# Finding the position to insert
# Inserting the label
# Printing user-facing output (UI concern)
# Hard to test: The function directly depends on the file system and user feedback (printing messages).
# Tightly coupled: Any change in logging, file handling, or insertion logic forces modification of the same function.
