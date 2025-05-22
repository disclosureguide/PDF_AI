from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from fastapi.responses import PlainTextResponse
from pdf.text_blob_extractor import TextBlobExtractor
from ai_summarizer import AiSummarizer

app = FastAPI()

@app.get("/hello", response_class=PlainTextResponse)
def hello_world():
    return "Hello World!"

@app.post("/extract-text", response_class=PlainTextResponse)
def extract_text_from_image(
    file: UploadFile = File(...),
    number_of_words: int = Query(30, description="Maximum number of words for the summary")
):
    try:
        extractor = TextBlobExtractor(file.file)
        text = extractor.run()
        summarizer = AiSummarizer(text)
        summary = summarizer.summarize(number_of_words)
        return summary
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 