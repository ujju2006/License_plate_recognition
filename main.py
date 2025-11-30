from detection import detect_plate

# List of all images you want to detect
images = [
    "images/Ford_licenseplate.jpg",
    "images/Hundai_license.jpg"
]

# Loop through each image and run detection
for img in images:
    print(f"Processing: {img}")
    detect_plate(img)
