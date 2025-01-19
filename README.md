WebP to PNG Converter Script
Overview
This script is designed to automate the process of converting all WebP images in a specified folder to PNG format, saving the converted files to a designated output folder. It leverages Python's powerful Pillow library for image processing.

Features
Converts all .webp images in a folder to .png format.
Ensures high-quality output in RGB color mode.
Automatically creates the output directory if it doesn’t exist.
Efficiently processes multiple files with real-time feedback.

Technology Used
Python: The primary programming language.
Pillow (PIL): A Python library for image processing.
OS module: To handle file and directory operations.
Code Snippet
python
Copier
Modifier
import os
from PIL import Image

# Input and output folder paths
input_folder = r"your/input/folder/path"
output_folder = r"your/output/folder/path"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".webp"):  # Check if the file is a WebP image
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".png"  # Replace .webp with .png
        output_path = os.path.join(output_folder, output_filename)

        # Open, convert, and save the image
        with Image.open(input_path).convert("RGB") as im:
            im.save(output_path, "png")
        print(f"Converted: {filename} -> {output_filename}")

print("Conversion complete!")
How It Works
Setup Input and Output Paths:

Specify the folder containing WebP images (input_folder).
Define the destination folder for PNG images (output_folder).
Image Processing:

The script iterates through all files in the input folder.
It identifies files with a .webp extension.
Each WebP file is opened, converted to RGB mode, and saved as a PNG file in the output folder.
Output:

The converted PNG images retain the original filenames but with a .png extension.
The script logs conversion progress in the console.
Usage
Install the required library:

bash
Copier
Modifier
pip install pillow
Modify the script:

Replace your/input/folder/path with the folder containing your WebP images.
Replace your/output/folder/path with the folder where you want the PNG images saved.
Run the script:

bash
Copier
Modifier
python your_script_name.py
Example Input and Output
Input:
Folder containing:

image1.webp
image2.webp

Output:
Folder containing:
image1.png
image2.png

Contact
For any questions or collaboration opportunities, feel free to connect with me on LinkedIn!
