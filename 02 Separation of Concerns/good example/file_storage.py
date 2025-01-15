def read_file(file_path: str) -> list[str]:
    """Reads all lines from the file and returns them as a list."""
    with open(file_path, "r") as f:
        return f.readlines()

def write_file(file_path: str, lines: list[str]) -> None:
    """Writes the given lines back to the file."""
    with open(file_path, "w") as f:
        f.writelines(lines)