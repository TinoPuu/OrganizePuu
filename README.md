# OrganizePuu

## Introduction
I made this project because I had thousands of images and videos synchronized from my phone to OneDrive over several years, all saved in a single, chaotic folder. With nearly **40,000 files** to sort through, manually organizing them was overwhelming. OrganizePuu was created to automatically organize and rename these images into categorized folders, saving time and reducing frustration.

## Purpose of the Project
OrganizePuu is designed to:
- Organizes images into subfolders with a custom number of pictures per folder.
- Renames images with a base name and sequential numbering.
- Preserves metadata (EXIF) like date, location, and camera details.
- Supports multiple image formats: `.jpg`, `.png`,`.jpeg` and `.heic`.

## How to Use
1. **Select the folder containing your images.**
2. **Choose the number of pictures per folder.**
3. **Enter the desired base name for the images.**
4. Sit back and let OrganizePuu do the work of organizing and renaming your photos.

## Setup and Installation

### Prerequisites
- **Python 3.x** installed on your system.
- **Pip** for package management.

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/tinpuu/organizepuu.git
   cd organizepuu
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```