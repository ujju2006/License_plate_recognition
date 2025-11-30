import cv2
import pytesseract

# Path to Tesseract (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\USER\Desktop\License_plate_recognition\tesseract.exe"

def detect_plate(image_path):
    # Load Haar Cascade for license plate
    plate_cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

    # Read the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect plates
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in plates:
        # Draw box
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Crop ROI
        plate_region = img[y:y+h, x:x+w]

        # OCR text
        plate_text = pytesseract.image_to_string(plate_region, config='--psm 8')
        print(f"Detected Number from {image_path}:", plate_text.strip())

        # Show cropped plate
        cv2.imshow(f"Plate - {image_path}", plate_region)

    # Show full result image
    cv2.imshow(f"Result - {image_path}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect_plate("images/Ford_Licenseplate.jpg")
detect_plate("images/Hyundai_License.jpg")
