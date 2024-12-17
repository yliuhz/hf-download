from huggingface_hub import hf_hub_download, snapshot_download
import joblib

REPO_ID = "Qwen/Qwen2-72B-Instruct"
# FILENAME = "sklearn_model.joblib"
REPO_ID = "Qwen/Qwen2.5-0.5B"

model = joblib.load(
    # hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    hf_hub_download(repo_id=REPO_ID)
)
