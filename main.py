from ai_summarizer import AiSummarizer
from pdf.text_pdf_extractor import TextPdfExtractor
from pdf.text_image_extractor import TextImageExtractor

# Define the image path
image_path = r"/Users/danieltuttle/projects/pdf_ai/data/comic.jpg"
pdf_path = r"/Users/danieltuttle/projects/pdf_ai/Seattle.pdf"

# Create an instance of TextImageExtractor and extract the text
extractor = TextImageExtractor(image_path)
text = extractor.run()

ai = AiSummarizer(text)
text = ai.summarize(50)

# te = TextPdfExtractor(pdf_path)
# pdf_text = te.run()

# ai = AiSummarizer(pdf_text)
# pdf_text = ai.summarize(50)

# print(text)
print(text)