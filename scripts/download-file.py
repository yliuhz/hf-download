### from https://huggingface.co/docs/huggingface_hub/en/guides/hf_file_system
### https://huggingface.co/docs/huggingface_hub/en/guides/download

import os
os.makedirs('temp', exist_ok=True)

from huggingface_hub import HfFileSystem
from huggingface_hub import hf_hub_download
fs = HfFileSystem()
f = open(f'temp/a.txt', 'w')

import traceback
from tqdm import tqdm

# List all files in a directory
paths = fs.ls("datasets/yubo2333/MMLongBench-Doc/documents", detail=False)
f.write(f'{paths}\n')
for path in tqdm(paths, total=len(paths)):
    filename = path.split('/')[-1]
    try:
        f.write(f'{hf_hub_download(repo_id="yubo2333/MMLongBench-Doc", subfolder="documents", filename=f"{filename}", repo_type="dataset", force_download=True)}\n')
    except Exception as e:
        f.write(f'Error: {path}, {traceback.format_exc()}\n') ## need manual download

paths = fs.ls("datasets/yubo2333/MMLongBench-Doc/data", detail=False)
f.write(f'{paths}\n')
for path in tqdm(paths, total=len(paths)):
    filename = path.split('/')[-1]
    try:
        f.write(f'{hf_hub_download(repo_id="yubo2333/MMLongBench-Doc", subfolder="data", filename=f"{filename}", repo_type="dataset", force_download=True)}\n')
    except Exception as e:
        f.write(f'Error: {path}, {traceback.format_exc()}\n') ## need manual download

# # List all ".csv" files in a repo
# fs.glob("datasets/my-username/my-dataset-repo/**/*.csv")

# # Read a remote file
# with fs.open("datasets/my-username/my-dataset-repo/data/train.csv", "r") as f:
#     train_data = f.readlines()

# # Read the content of a remote file as a string
# train_data = fs.read_text("datasets/my-username/my-dataset-repo/data/train.csv", revision="dev")

# # Write a remote file
# with fs.open("datasets/my-username/my-dataset-repo/data/validation.csv", "w") as f:
#     f.write("text,label")
#     f.write("Fantastic movie!,good")

f.close()