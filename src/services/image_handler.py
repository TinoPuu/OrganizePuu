import os
from PIL import Image
import pillow_heif
import piexif  # For full EXIF preservation
from src.config.settings import ALLOWED_EXTENSIONS
from src.utils.helpers import create_folder_if_not_exists, get_all_image_files
import sys
import time

# Register HEIC support with Pillow
pillow_heif.register_heif_opener()

def copy_image_with_metadata(src, dest, ext):
    """Copies an image while preserving its full metadata."""
    try:
        # Open the image and get its format
        image = Image.open(src)
        image_format = image.format
        
        # Extract EXIF data only for JPEG/JPG and HEIC
        exif_data = image.info.get("exif") if ext in [".jpg", ".jpeg", ".heic"] else None
        
        # Save the image to the destination
        image.save(dest, format=image_format, quality=95)
        image.close()
        
        # Reattach EXIF using piexif for full metadata preservation
        if exif_data:
            try:
                exif_dict = piexif.load(exif_data)
                exif_bytes = piexif.dump(exif_dict)
                piexif.insert(exif_bytes, dest)
            except Exception as e:
                print(f"⚠️ Warning: Failed to preserve EXIF for {src}. Skipping EXIF. Error: {e}")
        
    except Exception as e:
        print(f"❌ Error processing {src}: {e}")

def process_images(folder_path, folder_size, picture_name):
    folder_path = os.path.join(folder_path, '')  # Ensures trailing slash
    i, j, k = 0, 0, 0

    all_files = get_all_image_files(folder_path, ALLOWED_EXTENSIONS)
    total_files = len(all_files)

    if total_files == 0:
        print("❌ No images found in the selected folder.")
        return

    for index, filename in enumerate(all_files):
        ext = os.path.splitext(filename)[1].lower()
        FolderNumber = str(j)
        New_Folder = os.path.join(folder_path, FolderNumber)

        create_folder_if_not_exists(New_Folder)

        Number = str(k)
        old_name = os.path.join(folder_path, filename)
        new_name = os.path.join(New_Folder, f"{picture_name} {Number}{ext}")

        if os.path.exists(new_name):
            print(f"❌ Error: File with the name {new_name} already exists. Skipping...")
            continue

        # Only attempt EXIF preservation for supported formats
        if ext in [".jpg", ".jpeg", ".heic"]:
            copy_image_with_metadata(old_name, new_name, ext)
        else:
            # Directly copy PNG without EXIF
            try:
                image = Image.open(old_name)
                image.save(new_name, quality=95)
                image.close()
            except Exception as e:
                print(f"❌ Error processing {old_name}: {e}")

        i += 1
        k += 1

        if i == folder_size:
            i = 0
            j += 1

        # Display progress with a fun animation
        progress = int(((index + 1) / total_files) * 100)
        animation = "🌈"
        sys.stdout.write(f"\r🖼️ Processing... Progress: {progress}% ({index + 1}/{total_files}) {animation}")
        sys.stdout.flush()
        time.sleep(0.1)

    print()  # Move to the next line after progress
