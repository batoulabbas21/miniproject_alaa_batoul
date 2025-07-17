import os
from transformers import AutoTokenizer, AutoModel, AutoModelForSeq2SeqLM

# Change this to your desired base path
base_path = os.path.join(os.getcwd(), r"C:\Users\user\my_project")


from transformers import AutoTokenizer, AutoModel, AutoModelForSeq2SeqLM, AutoModelForTokenClassification

# 🔧 Set your base path here
BASE_PATH = os.path.join(os.getcwd(), "my_models")

# ----------- Model 1: BART Large CNN (Summarization) -----------
summ_model_name = "facebook/bart-large-cnn"
summ_save_path = os.path.join(BASE_PATH, "bart-large-cnn")

summ_tokenizer = AutoTokenizer.from_pretrained(summ_model_name)
summ_model = AutoModelForSeq2SeqLM.from_pretrained(summ_model_name)

summ_tokenizer.save_pretrained(summ_save_path)
summ_model.save_pretrained(summ_save_path)

# ----------- Model 2: ClinicalBERT (Classification / Embedding) -----------
bert_model_name = "emilyalsentzer/Bio_ClinicalBERT"
bert_save_path = os.path.join(BASE_PATH, "Bio_ClinicalBERT")

bert_tokenizer = AutoTokenizer.from_pretrained(bert_model_name)
bert_model = AutoModel.from_pretrained(bert_model_name)

bert_tokenizer.save_pretrained(bert_save_path)
bert_model.save_pretrained(bert_save_path)

# ----------- Model 3: BioBERT NER -----------
ner_model_name = "d4data/biobert-ner"
ner_save_path = os.path.join(BASE_PATH, "biobert-ner")

ner_tokenizer = AutoTokenizer.from_pretrained(ner_model_name)
ner_model = AutoModelForTokenClassification.from_pretrained(ner_model_name)

ner_tokenizer.save_pretrained(ner_save_path)
ner_model.save_pretrained(ner_save_path)

print(f" All models downloaded and saved under: {BASE_PATH}")
