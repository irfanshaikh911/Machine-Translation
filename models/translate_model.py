from transformers import MarianMTModel, MarianTokenizer

# Model for English to Hindi
model_name = "Helsinki-NLP/opus-mt-en-hi"

tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)