import os
import shutil
import re

# Optional: download sample files using requests (if needed)
# import requests
# Example: requests.get(url).content -> save to file

# Folder to organize
source_folder = "Downloads"  # Change to your folder path

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def sanitize_filename(name):
    """Remove invalid characters from filenames"""
    return re.sub(r'[<>:"/\\|?*]', "_", name)

def organize_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(folder, category)
                    os.makedirs(target_folder, exist_ok=True)
                    safe_name = sanitize_filename(filename)
                    target_path = os.path.join(target_folder, safe_name)
                    # Handle duplicates
                    count = 1
                    base, ext = os.path.splitext(safe_name)
                    while os.path.exists(target_path):
                        target_path = os.path.join(target_folder, f"{base}_{count}{ext}")
                        count += 1
                    shutil.move(file_path, target_path)
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                safe_name = sanitize_filename(filename)
                target_path = os.path.join(other_folder, safe_name)
                count = 1
                base, ext = os.path.splitext(safe_name)
                while os.path.exists(target_path):
                    target_path = os.path.join(other_folder, f"{base}_{count}{ext}")
                    count += 1
                shutil.move(file_path, target_path)
    print("Files have been organized successfully!")

# Run the organizer
organize_files(source_folder)
