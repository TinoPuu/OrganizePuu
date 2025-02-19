import tkinter as tk
from tkinter import filedialog


def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Image Folder")
    return folder_path


def get_user_inputs():
    folder_path = select_folder()
    if not folder_path:
        print("No folder selected. Exiting...")
        exit()
    folder_size = int(input("How many pictures per folder? "))
    picture_name = input("Which name do you want for your pictures? ")
    return folder_path, folder_size, picture_name
