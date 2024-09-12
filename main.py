import os
import re
import sys
import shutil
from datetime import datetime

# Define video and subtitle file extensions
video_extensions = ['.mkv', '.mp4', '.avi', '.mov']
subtitle_extensions = ['.srt', '.sub', '.ass', '.vtt']

# Regular expression pattern to match titles, season and episode info
pattern = re.compile(r'(?P<title>.*?)[._\s-]*[sS](?P<season>\d{2})[eE](?P<episode>\d{2})')

def check_and_rename_file(file_name):
    file_extension = os.path.splitext(file_name)[1].lower()

    # Check if the file is a video or subtitle based on the extension
    if file_extension in video_extensions or file_extension in subtitle_extensions:
        # Extract title, season, and episode from filename
        match = pattern.search(file_name)
        if match:
            title = match.group('title').replace('.', ' ').replace('_', ' ').replace('-', ' ').strip()  # Clean up title
            season = match.group('season')
            episode = match.group('episode')

            # Capitalize each word in the title
            title = ' '.join([word.capitalize() for word in title.split()])

            # Construct the new file name
            new_file_name = f'{title} s{season} e{episode}{file_extension}'

            return new_file_name
    return None

def create_backup_folder(directory):
    # Create a backup folder named "backup_<timestamp>" in the given directory
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(directory, f'backup_{timestamp}')

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Backup folder created: {backup_folder}")

    return backup_folder

def backup_files(directory, backup_folder):
    # Iterate over all files in the directory and move them to the backup folder
    for file_name in os.listdir(directory):
        old_file_path = os.path.join(directory, file_name)

        # Only back up files, ignore directories
        if os.path.isfile(old_file_path):
            backup_file_path = os.path.join(backup_folder, file_name)
            shutil.copy2(old_file_path, backup_file_path)  # Copy the file to the backup folder
            print(f'Backed up: {file_name} to {backup_folder}')

def rename_files_in_directory(directory):
    # Create a backup folder and back up all files before renaming
    backup_folder = create_backup_folder(directory)
    backup_files(directory, backup_folder)

    # Iterate over all files in the given directory
    for file_name in os.listdir(directory):
        new_name = check_and_rename_file(file_name)
        if new_name:
            # Get the full file paths
            old_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {file_name} -> {new_name}')

# Main script
if __name__ == "__main__":
    # Check if a directory path is passed as an argument
    if len(sys.argv) < 2:
        print("Usage: python rename_files.py <directory_path>")
        sys.exit(1)

    # Get the directory path from command-line arguments
    directory_path = sys.argv[1]

    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    # Call the function to rename files in the specified directory
    rename_files_in_directory(directory_path)
