# 🛰️ Satellite Super-Resolution using SRGAN

This project implements a **Super-Resolution Generative Adversarial Network (SRGAN)** for enhancing the resolution of satellite images. It is built with the goal of generating high-resolution (HR) satellite images from their low-resolution (LR) counterparts.

---

## 📁 Project Structure

```
Satellite-Super-Resolution-SRGAN
├── 🐍 srgan.py            # Main SRGAN implementation (training & inference)
├── 🐍 split_image.py      # Utility to split images into patches (HR/LR pairs)
├── 📜 README.md           # Project documentation
└── 📂 data
    └── [Dataset from Kaggle]
```

---

## 📦 Dataset

We use a satellite image dataset available on Kaggle:

🔗 [Satellite Super Resolution - Khazani](https://www.kaggle.com/datasets/khazaniahmedibrahim/satellite-super-resolution-khazani)

- Contains high-resolution satellite images.
- Used to generate LR-HR pairs for training the SRGAN model.

---

## 🛠 Requirements

Make sure you have the following installed:

- Python >= 3.7
- TensorFlow or PyTorch (depending on your implementation)
- NumPy
- OpenCV
- Matplotlib
- tqdm
- PIL (Pillow)



