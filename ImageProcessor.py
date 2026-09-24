import os
import cv2

input_Folder = "input_Images"
output_Folder = "output_Images"

os.makedirs(output_Folder, exist_ok = True)

for filename in os.listdir(input_Folder):

    if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp")):
        input_path = os.path.join(input_Folder, filename)
        img = cv2.imread(input_path)

        if img is None:
            print(f"Could not Read {filename}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        resized = cv2.resize(gray, (300,300))

        output_path = os.path.join(output_Folder, filename)

        cv2.imwrite(output_path, resized)

        print(f"Processed: {filename}")

print("Batch Process Completed")