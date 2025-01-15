from file_storage import read_file, write_file
from cad_parser import find_insertion_index, insert_label

def run_label_insertion(file_path: str, search_term: str, new_label: str) -> None:
    print("[UI] Starting label insertion...")

    # 1. Read lines from the file
    lines = read_file(file_path)
    print("[UI] File has been read successfully.")

    # 2. Find insertion index
    insertion_index = find_insertion_index(lines, search_term)
    if insertion_index is None:
        print(f"[UI] Search term '{search_term}' not found. No label will be inserted.")
        return

    # 3. Insert the new label at the found position
    updated_lines = insert_label(lines, insertion_index, new_label)
    print(f"[UI] Label '{new_label}' inserted after '{search_term}' at index {insertion_index}.")

    # 4. Write the updated lines back to the file
    write_file(file_path, updated_lines)
    print(f"[UI] Changes written to {file_path}.")

if __name__ == "__main__":
    # Example usage
    run_label_insertion(
        file_path="cad_savefile.txt",
        search_term="#INSERT_LABEL_HERE",
        new_label="#NEW_LABEL: MyCustomLabel"
    )