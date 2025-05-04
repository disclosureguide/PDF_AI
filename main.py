from ai_summarizer import AiSummarizer
from text_image_extractor import TextImageExtractor

# Define the image path
image_path = r"/Users/danieltuttle/projects/pdf_ai/comic.jpg"

# Create an instance of TextImageExtractor and extract the text
extractor = TextImageExtractor(image_path)
text = extractor.run()

summarizer = AiSummarizer(text)
text = summarizer.summarize(50)
# Display the extracted text
print(text)