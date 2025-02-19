import os


def create_folder_if_not_exists(folder_path):
    """Creates a folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"📂 Created new directory: {folder_path}")


def get_all_image_files(directory, allowed_extensions):
    """Returns a list of image files in a directory with allowed extensions."""
    return [
        file
        for file in os.listdir(directory)
        if os.path.splitext(file)[1].lower() in allowed_extensions
    ]
