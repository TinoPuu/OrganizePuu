from src.services.input_handler import get_user_inputs
from src.services.image_handler import process_images


def print_banner():
    banner = r"""
🌲 Welcome to OrganizePuu - Picture Organizer! 🌲
----------------------------------------------------------
"""
    print(banner)


def print_completion():
    print("\n🚀 All images have been organized successfully! ")


def main():
    print_banner()  # Display startup banner
    folder_path, folder_size, picture_name = get_user_inputs()
    process_images(folder_path, folder_size, picture_name)
    print_completion()  # Display completion message


if __name__ == "__main__":
    main()
