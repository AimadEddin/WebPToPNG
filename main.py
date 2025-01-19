import os
from PIL import Image

# Input and output folder paths
input_folder = r"C:\Users\......"
output_folder = r"C:\Users\....."

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
