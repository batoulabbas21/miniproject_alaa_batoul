# download_ner_model.py
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="d4data/biomedical-ner-all",
    repo_type="model",
    local_dir="my_models/biomedical-ner-all"
)

print("neuronal NER model is ready offline!")
