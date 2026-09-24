from tkinter import Tk, filedialog

# Hide the main Tkinter window
root = Tk()
root.withdraw()

# Open file dialog to select multiple images
image_paths = filedialog.askopenfilenames(
    title="Select Images",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
        ("All Files", "*.*")
    ]
)

# Check if any images were selected
if not image_paths:
    print("No images selected.")
    exit()

print("Selected Images:")

for image in image_paths:
    print(image)