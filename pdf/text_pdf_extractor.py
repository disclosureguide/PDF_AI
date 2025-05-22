import PyPDF2

class TextPdfExtractor:
    def __init__(self, file_path):
        """
        Initialize the TestPdfExtractor with a PDF file path.
        
        Args:
            file_path (str): Path to the PDF file to process
        """
        self.file_path = file_path
        
    def run(self):
        """
        Extract text from the PDF file.
        
        Returns:
            str: Extracted text from the PDF
        """
        try:
            # Open the PDF file in binary read mode
            with open(self.file_path, 'rb') as file:
                # Create a PDF reader object
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Get the number of pages in the PDF
                num_pages = len(pdf_reader.pages)
                
                # Extract text from all pages
                text = ""
                for page_num in range(num_pages):
                    # Get the page object
                    page = pdf_reader.pages[page_num]
                    # Extract text from the page
                    text += page.extract_text()
                    
                return text.strip()
                
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")

