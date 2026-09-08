# Benchmarking Pretrained CLIP on Apple Silicon

An empirical performance engineering benchmark evaluating the inference efficiency, latency trade-offs, and computational footprints of local zero-shot image classification using pretrained CLIP (ViT-B/32). This project systematically compares single-threaded x86/ARM CPU performance boundaries against the hardware-accelerated **Metal Performance Shaders (MPS)** device backend.

---

## 🛠️ Hardware & Environment Profile
All benchmark evaluation configurations are bounded strictly to the following local hardware execution environment:
* **System-on-Chip (SoC):** Apple M2 Max (12-Core CPU: 8 Performance, 4 Efficiency; 38-Core GPU)
* **Memory Architecture:** Unified Memory Architecture (UMA)
* **Operating System:** macOS Sonoma / Sequoia
* **Software Backend:** PyTorch Native MPS (`torch.device("mps")`) paired with a local MLflow Tracking Instance

---

## 📂 Project Architecture
The codebase follows a standard, decoupled machine learning lifecycle layout driven entirely via a central configuration file:

```text
clip-apple-silicon-benchmarks/
├── config/
│   └── main_config.yaml      # Central execution parameters (device, prompts, batches)
├── src/
│   ├── __init__.py
│   ├── data_loader.py        # Dataset acquisition and profiling pipeline
│   ├── model_loader.py       # Pretrained CLIP weight initialization
│   └── inference_engine.py   # Core zero-shot evaluation loop calculating cosine similarity
├── requirements.txt          # Absolute local package dependencies
└── README.md                 # System overview and deployment guide
```

---

## 🚀 Setup & Execution Instructions

### 1. Initialize Local Environment
Clone the repository and install the verified software dependencies using `pip`:
```bash
git clone https://github.com
cd clip-apple-silicon-benchmarks
pip install -r requirements.txt
```