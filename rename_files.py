import os
import sys
from pathlib import Path

def rename_files_sequentially(directory: str, prefix: str = "file", extension: str = None, start: int = 1) -> None:
    """
    Rename all files in a directory sequentially.

    Args:
        directory: Path to the directory containing files
        prefix: Prefix for the new filenames (default: "file")
        extension: File extension to filter by (e.g., ".txt"). If None, renames all files.
        start: Starting number for the sequence (default: 1)
    """
    dir_path = Path(directory)

    if not dir_path.exists():
        print(f"Error: Directory '{directory}' does not exist")
        return

    if not dir_path.is_dir():
        print(f"Error: '{directory}' is not a directory")
        return

    # Get all files (not directories)
    files = [f for f in dir_path.iterdir() if f.is_file()]

    if extension:
        # Filter by extension (with or without dot)
        if not extension.startswith('.'):
            extension = '.' + extension
        files = [f for f in files if f.suffix == extension]

    # Sort files alphabetically for consistent ordering
    files.sort()

    if not files:
        print("No files found to rename")
        return

    print(f"Renaming {len(files)} files in '{directory}'...")

    for i, file_path in enumerate(files, start=start):
        old_name = file_path.name
        ext = file_path.suffix if file_path.suffix else ""
        new_name = f"{prefix}_{i:03d}{ext}"
        new_path = dir_path / new_name

        # Handle name conflicts
        counter = 1
        while new_path.exists() and new_path != file_path:
            new_name = f"{prefix}_{i:03d}_{counter}{ext}"
            new_path = dir_path / new_name
            counter += 1

        os.rename(file_path, new_path)
        print(f"  {old_name} -> {new_name}")

    print("Done!")


if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python rename_files.py <directory> [prefix] [extension] [start]")
        print("Example: python rename_files.py ./images photo jpg 1")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else "file"
    extension = sys.argv[3] if len(sys.argv) > 3 else None
    start = int(sys.argv[4]) if len(sys.argv) > 4 else 1

    rename_files_sequentially(directory, prefix, extension, start)
