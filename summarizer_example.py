from ai_summarizer import AiSummarizer
from text_image_extractor import TextImageExtractor

def main():
    # First extract text from an image
    image_path = r"/Users/danieltuttle/projects/pdf_ai/comic.jpg"
    extractor = TextImageExtractor(image_path)
    extracted_text = extractor.run()
    
    # Now summarize the extracted text
    summarizer = AiSummarizer(extracted_text)
    summary = summarizer.summarize(30)  # Get a 30-word summary
    
    print("Original Text:")
    print(extracted_text)
    print("\nSummarized Text:")
    print(summary)

if __name__ == "__main__":
    main() 