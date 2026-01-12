# Android Ransomware Detection Using Deep Learning (ViT + CNN)

This repository presents a hybrid deep learning approach to detect **Android ransomware** by transforming **CuckooDroid** sandbox reports into image representations and classifying them using **Convolutional Neural Networks (CNNs)** and **Vision Transformers (ViT)**.

**Accepted at ICDAM 2025** — _"From Behavior to Pixels: A Vision Transformer Approach for Android Ransomware Detection"_

---

## Project Summary

This project aims to accurately detect Android ransomware by analyzing behavior reports. It uses both classical ML on structured data and advanced deep learning models on visualized report data.

### Key Highlights

- **Behavioral Reports:** 4200 sandboxed JSON files (2000 benign, 2200 ransomware) from **CuckooDroid**.
- **Traditional ML:** Converted JSON to CSV and trained a **Random Forest classifier** (Accuracy: 99.41%).
- **Image-Based DL:**
  - Transformed JSON reports into **RGB & Grayscale images**.
  - Applied **CNN** and **ViT** models.
  - Achieved **99.78% accuracy** with Vision Transformer.

---

## Dataset

- **Source:** Generated using CuckooDroid sandbox on custom APKs.
- **Format:** `.json` → `.csv` & `.png`
- **Labels:** `Benign` / `Ransomware`

---

## Experiments & Results

![Performace matrices](/matrices.png)

---

## Tech Stack

- **CuckooDroid** – Behavior analysis
- **Python**, **Pandas**, **Scikit-learn**
- **Matplotlib**, **Pillow** – JSON to Image
- **TensorFlow / Keras**, **PyTorch** – DL Models
- **ViT**, **CNN**
- **Random Forest** – Classical ML

---

## How It Works

### 1. **Data Collection**
   - Executed 4200 APKs in CuckooDroid sandbox.
   - Extracted `.json` behavior reports.

### 2. **Classical Machine Learning**
   - Converted JSON → tabular CSV.
   - Trained Random Forest model.

### 3. **Deep Learning Pipeline**
   - Transformed JSON into images (RGB and Grayscale).
   - Trained CNN and Vision Transformer models for classification.

---

## Achievements

- **Accepted at ICDAM 2025**
- **ViT achieved 99.78% accuracy** — proving visual representations of behavior data are highly effective.

---
