
This Python script renames video and subtitle files based on their title, season number, and episode number. Additionally, it creates a backup folder before performing any renaming to ensure that the original files are preserved.

## Features

- **Automatic File Renaming**: Detects video and subtitle files and renames them in the format `Title sXX eXX.ext` (e.g., `Friends s01 e01.mkv`), using the `guessit` library to handle various filename formats.
- **Title Normalization**: Handles titles with multiple words and different separators (dots, underscores, hyphens) without relying on static patterns or regular expressions.
- **File Backup**: Before renaming, all files are copied to a backup folder in the same directory with a timestamp to avoid overwriting backups from different runs.
- **Supported File Types**: Renames common video formats (e.g., `.mkv`, `.mp4`, `.avi`) and subtitle formats (e.g., `.srt`, `.sub`, `.ass`).

## Requirements

- Python 3.x
- `guessit` library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `guessit` library:
   ```bash
   pip install guessit
   ```
3. Clone or download this repository to your local machine.

## Usage

### Command-Line Usage

To use the script, open a terminal or command prompt and run the following command:

```bash
python rename_files_with_backup.py <directory_path>
```

Replace `<directory_path>` with the full path to the directory containing the video and subtitle files you want to rename.

### Example

If your files are located in `/Users/username/Movies/TVShows`, run the script like this:

```bash
python rename_files_with_backup.py /Users/username/Movies/TVShows
```

### File Format

The script renames files that match a variety of patterns using the `guessit` library to extract details. For example:

- Original: `friends.s01e01.720p.bluray.mkv`
- Renamed: `Friends s01 e01.mkv`

- Original: `The-Office_S02E05_1080p.mkv`
- Renamed: `The Office s02 e05.mkv`

### Backup

Before renaming, the script will create a backup folder named `backup_<timestamp>` in the provided directory and copy all files into this folder. This ensures that original files are preserved.

Example backup folder:

```
/path/to/your/files/backup_20230912_153015
```

## Supported File Types

The script recognizes the following file extensions:

- **Video Files**: `.mkv`, `.mp4`, `.avi`, `.mov`
- **Subtitle Files**: `.srt`, `.sub`, `.ass`, `.vtt`

## Notes

- The script relies on `guessit` to extract titles, season, episode, and other metadata from filenames based on various patterns and conventions.
- Ensure that the directory path is valid and contains files that match the expected naming conventions for TV shows or movies.


