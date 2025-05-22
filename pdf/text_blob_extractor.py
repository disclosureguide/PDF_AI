from PIL import Image
from pytesseract import pytesseract

class TextBlobExtractor:
    def __init__(self, image_file):
        """
        Initialize the TextBlobExtractor with an image file object.
        
        Args:
            image_file (file-like object): An image file object to process
        """
        self.image_file = image_file
        # Setting the path to tesseract executable
        self.tesseract_path = r"/opt/homebrew/Cellar/tesseract/5.5.0_1/bin/tesseract"
        pytesseract.tesseract_cmd = self.tesseract_path
        
    def run(self):
        """
        Extract text from the image file object.
        
        Returns:
            str: Extracted text from the image
        """
        try:
            # Opening and processing the image from the file object
            img = Image.open(self.image_file)
            # Extract text from the image
            text = pytesseract.image_to_string(img)
            # Return the text without the trailing newline
            return text.strip()
        except Exception as e:
            raise Exception(f"Error processing image: {str(e)}") 