
import sys
print("PYTHON:", sys.executable)

import torch
print("TORCH:", torch.__version__)
print("CUDA:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))

# (ai) PS C:\Users\okss2\OneDrive\바탕 화면\test\0227> python test.py
# PYTHON: C:\AI\envs\ai\python.exe
# TORCH: 2.5.1+cu121
# CUDA: True
# GPU: NVIDIA GeForce RTX 3060
# (ai) PS C:\Users\okss2\OneDrive\바탕 화면\test\0227>     