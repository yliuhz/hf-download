# Downloading scripts for Models and Datasets on Hugging-Face




For some repositories, their may be errors during downloading as below: 

```{text}
OSError: Consistency check failed: file should be of size 11191551 but has size 15398470 ((…)sionsources-121120210508-phpapp02_95.pdf).
This is usually due to network issues while downloading the file. Please retry with `force_download=True`.
```

In this case, use the script in `scripts/download-file.py` to download files one by one. Those files with errors need to be download manually by clicking buttons on hugging face. The file lists that have troubles will be stored in `temp/a.txt`.

```{bash}
python -u scripts/download-file.py
```

![example](assets/example.png)



## Normal downloading

Normally, one could use the script `scripts/download.sh`.

```{bash}
bash scripts/download.sh <repo_id> <repo_type>
```
