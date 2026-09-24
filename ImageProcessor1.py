import cv2
import os
from tkinter import Tk, filedialog, simpledialog

root = Tk()
root.withdraw()

image_paths = filedialog.askopenfilenames(
    title="Select Images",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp"),
        ("All Files", "*.*")
    ]
)

if not image_paths:
    print("No images selected.")
    exit()

output_folder = filedialog.askdirectory(
    title="Select Output Folder"
)

if not output_folder:
    print("No output folder selected.")
    exit()

width = simpledialog.askinteger("Resize", "Enter Width: ")
height = simpledialog.askinteger("Resize", "Enter Height: ")

if(width is None or height is None):
    print("Resize Cancelled")
    exit()

for image_path in image_paths:

    image = cv2.imread(image_path)

    if image is None:
        print(f"Could not read {image_path}")
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.resize(gray, (width, height))

    filename = os.path.basename(image_path)

    save_path = os.path.join(output_folder, filename)
    cv2.imwrite(save_path, gray)

    print(f"Saved: {save_path}")

print("\nAll selected images have been processed successfully.")