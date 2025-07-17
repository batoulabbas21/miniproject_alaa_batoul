import requests
import os

folder_path = r"C:\Users\user\my_project\sample_reports" 
url = "http://127.0.0.1:8000/analyze/"

for filename in os.listdir(folder_path):
    path = os.path.join(folder_path, filename)
    with open(path, "rb") as f:
        files = {"file": (filename, f)}
        r = requests.post(url, files=files)
        print(f"✅ Uploaded {filename} — Response:")
        print(r.json())
