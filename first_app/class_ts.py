from transformers import pipeline

class Prediction():
    def __init__(self) -> None:
        self.model_path = '../all_model/anil/bart-large-cnn'
        self.summarizer = pipeline("summarization", model=self.model_path)

    def process(self,input_text):
        output = self.summarizer(input_text, max_length=70, min_length=30, do_sample=False)
        return output




