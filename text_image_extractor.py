from PIL import Image 
from pytesseract import pytesseract 

class TextImageExtractor:
    def __init__(self, image_path):
        """
        Initialize the TextImageExtractor with an image path.
        
        Args:
            image_path (str): Path to the image file to process
        """
        self.image_path = image_path
        # Setting the path to tesseract executable
        self.tesseract_path = r"/opt/homebrew/Cellar/tesseract/5.5.0_1/bin/tesseract"
        pytesseract.tesseract_cmd = self.tesseract_path
        
    def run(self):
        """
        Extract text from the image file.
        
        Returns:
            str: Extracted text from the image
        """
        try:
            # Opening and processing the image
            img = Image.open(self.image_path)
            # Extract text from the image
            text = pytesseract.image_to_string(img)
            # Return the text without the trailing newline
            return text.strip()
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}")
