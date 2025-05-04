from gpt4all import GPT4All

class AiSummarizer:
    def __init__(self, text):
        """
        Initialize the AiSummarizer with the text to be summarized.
        
        Args:
            text (str): The text content to be summarized
        """
        self.text = text
        # Initialize the GPT4All model with a good model for summarization
        self.model = GPT4All("orca-mini-3b-gguf2-q4_0")
        
    def summarize(self, number_of_words):
        """
        Summarize the text to be less than the specified number of words.
        
        Args:
            number_of_words (int): Maximum number of words for the summary
            
        Returns:
            str: Summarized text
        """
        try:
            # Create the prompt for summarization
            prompt = f"""Please summarize the following text in less than {number_of_words} words. 
            Keep the most important information while maintaining coherence.
            
            Text to summarize:
            {self.text}
            
            Summary:"""
            
            # Generate the summary using GPT4All
            response = self.model.generate(
                prompt=prompt,
                max_tokens=number_of_words * 4,  # Providing some buffer for generation
                temp=0.7,
                top_k=40,
                top_p=0.4,
                repeat_penalty=1.18
            )
            
            # Clean up the response and ensure it meets the word count requirement
            summary = response.strip()
            words = summary.split()
            if len(words) > number_of_words:
                summary = ' '.join(words[:number_of_words])
            
            return summary
            
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")
