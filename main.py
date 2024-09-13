import os
import sys
from guessit import guessit
import shutil
from datetime import datetime

# Define video and subtitle file extensions
video_extensions = ['.mkv', '.mp4', '.avi', '.mov']
subtitle_extensions = ['.srt', '.sub', '.ass', '.vtt']

def check_and_rename_file(file_name):
    # Use guessit to extract details from the file name
    details = guessit(file_name)

    # Check if the file is a video or subtitle based on the extension
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension in video_extensions or file_extension in subtitle_extensions:
        if 'title' in details and 'season' in details and 'episode' in details:
            title = details['title']
            season = details['season']
            episode = details['episode']

            # Construct the new file name
            new_file_name = f'{title} s{season:02d} e{episode:02d}{file_extension}'
            return new_file_name
    return None

def create_backup_folder(directory):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(directory, f'backup_{timestamp}')

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Backup folder created: {backup_folder}")

    return backup_folder

def backup_files(directory, backup_folder):
    for file_name in os.listdir(directory):
        old_file_path = os.path.join(directory, file_name)

        if os.path.isfile(old_file_path):
            backup_file_path = os.path.join(backup_folder, file_name)
            shutil.copy2(old_file_path, backup_file_path)  # Copy the file to the backup folder
            print(f'Backed up: {file_name} to {backup_folder}')

def rename_files_in_directory(directory):
    backup_folder = create_backup_folder(directory)
    backup_files(directory, backup_folder)

    for file_name in os.listdir(directory):
        new_name = check_and_rename_file(file_name)
        if new_name:
            old_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_name)

            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {file_name} -> {new_name}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rename_files.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        sys.exit(1)

    rename_files_in_directory(directory_path)
