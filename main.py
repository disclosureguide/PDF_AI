from PIL import Image 
from pytesseract import pytesseract 
  
# Defining paths to tesseract executable
# and the image we would be using 
path_to_tesseract = r"/opt/homebrew/Cellar/tesseract/5.5.0_1/bin/tesseract"
image_path = r"/Users/danieltuttle/projects/pdf_ai/comic.jpg"
  
# Opening the image & storing it in an image object 
img = Image.open(image_path) 
  
# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 
  
# Passing the image object to image_to_string() function 
# This function will extract the text from the image 
text = pytesseract.image_to_string(img) 
  
# Displaying the extracted text 
print(text[:-1])