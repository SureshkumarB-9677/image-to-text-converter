!sudo apt install tesseract-ocr
!pip install pytesseract

import pytesseract
from PIL import Image

def image_to_text(image_path):

  img = Image.open(image_path)
  text = pytesseract.image_to_string(img)
  return text


image_path = 'path/to/your/image.jpg' 
extracted_text = image_to_text(image_path)
print(extracted_text)