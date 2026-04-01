# Slim-Shady

My collection of useful scripts and projects.

## Scripts

### rename_files.py

Rename files in a directory sequentially.

```bash
python rename_files.py <directory> [prefix] [extension] [start]
```

**Arguments:**
- `directory` — folder containing files (required)
- `prefix` — prefix for new filenames (default: "file")
- `extension` — filter by extension (e.g., "jpg", "pdf")
- `start` — starting number (default: 1)

**Examples:**

```bash
# Rename all files
python rename_files.py ./my_folder

# Rename only .jpg files with prefix "photo"
python rename_files.py ./images photo jpg

# Start from 100
python rename_files.py ./files doc pdf 100
```

## License

MIT
