from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("nbroad/ESG-BERT")

model = AutoModelForSequenceClassification.from_pretrained("nbroad/ESG-BERT")