import io
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image, ImageFilter

# 🔧 Explicitly set the path to Tesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\tesseract\tesseract.exe"

def extract_text_from_pdf(file_bytes: bytes, dpi: int = 300) -> str:
    images = convert_from_bytes(file_bytes, dpi=dpi, poppler_path=r"C:\Users\user\poppler\poppler-24.08.0\Library\bin")  
    text_pages = []
    for img in images:
        img = img.convert("L").filter(ImageFilter.SHARPEN)  # Enhance image for better OCR
        text = pytesseract.image_to_string(img, config="--psm 6")
        text_pages.append(text)
    return "\n\n".join(text_pages)
