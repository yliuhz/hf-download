#!/bin/bash

# REPO=Qwen/Qwen2.5-0.5B
# REPO=Qwen/Qwen2.5-72B-Instruct
# REPO=meta-llama/Llama-3.1-70B-Instruct
REPO=$1
TYPE=$2
LOCALDIR=$3
# REPO=meta-llama/Llama-3.1-8B-Instruct
# REPO=Qwen/Qwen2-72B-Instruct
# REPO=Qwen/Qwen2-7B-Instruct
# HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download $REPO --include "*.safetensors*" 
# HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download $REPO --include "*.json" 

if [[ -z $TYPE ]]; then
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download $REPO --include "*" 
else
if [[ -z $LOCALDIR ]]; then
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download $REPO --include "*" --repo-type $TYPE
else
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download $REPO --include "*" --repo-type $TYPE --local-dir $LOCALDIR
fi
fi


