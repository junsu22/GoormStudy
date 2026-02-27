
 딥러닝 수업 대비: 크레딧 아끼려고 하이브리드(로컬+코랩)로 실습 진행
 - 파이프라인 연습 중이라 디버깅이 많음
 - 딥러닝 학습 자체는 코랩 예정(환경 통일)
 - 로컬은 ML/코드흐름 연습 + 필요시 GPU도 사용 가능하게 준비

 [1] conda 환경 구축 (호환 안정: Python 3.12 → 3.10)
 conda create -n ai python=3.10 -y
 conda activate ai

 [2] 머신러닝 기본 라이브러리
 pip install numpy pandas matplotlib seaborn scikit-learn jupyterlab

 [3-A] (선택) 로컬 CPU로만 PyTorch 설치 (가벼운 구조/흐름 연습용)
 pip install torch torchvision torchaudio
 - 설치 후 torch 버전 예: 2.x.x+cpu
 - torch.cuda.is_available() == False 정상

 [GPU 확인] 내 PC GPU/드라이버 체크
 nvidia-smi
 - RTX 3060 확인
 - Driver 560.94 / CUDA Version 12.6 표시

 [3-B] (선택) 로컬 GPU로 PyTorch 갈아타기 (CUDA 지원 wheel 설치)
 (기존 CPU 버전 torch 제거 후 진행)
 pip uninstall -y torchaudio torchvision torch
 pip uninstall -y torchaudio torchvision torch   보험용

 pip install --upgrade pip
 pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

 [버전/인식 확인]
 python -c "import torch; print(torch.__version__)"
 - 기대: 2.x.x+cu121

 python -c "import torch; print('CUDA:', torch.cuda.is_available()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'no gpu')"
 - 기대: CUDA: True / NVIDIA GeForce RTX 3060

 [실행]
 jupyter lab

 [디버깅 체크포인트]
 python -c "import sys; print(sys.executable)"
 - 기대:


  C:\AI\envs\ai\python.exe
