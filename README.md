# Android Ransomware Detection Using Deep Learning (ViT + CNN)

This repository presents a hybrid deep learning approach to detect **Android ransomware** by transforming **CuckooDroid** sandbox reports into image representations and classifying them using **Convolutional Neural Networks (CNNs)** and **Vision Transformers (ViT)**.

**Published at ICDAM 2025 (Springer LNNS)** — [_"From Behavior to Pixels: A Vision Transformer Approach for Android Ransomware Detection"_](https://link.springer.com/chapter/10.1007/978-3-032-03072-6_11) by Satyam Kesharwani (lead and corresponding author), Kamaldeep and Manisha Malik.

📝 **Full write-up:** [From Behavior to Pixels: Android Ransomware Detection with a Vision Transformer](https://www.satyamk.dev/blog/android-ransomware-detection-vision-transformer), covering the pipeline, the image encoding, the four models and how to read the results.

---

## Project Summary

This project aims to accurately detect Android ransomware by analyzing behavior reports. It uses both classical ML on structured data and advanced deep learning models on visualized report data.

### Key Highlights

- **Behavioral Reports:** 4,280 sandboxed JSON reports (2,280 ransomware from RansomProber, 2,000 benign from AndroZoo) from **CuckooDroid**.
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
   - Executed 4,280 APKs in the CuckooDroid sandbox.
   - Extracted `.json` behavior reports.

### 2. **Classical Machine Learning**
   - Converted JSON → tabular CSV.
   - Trained Random Forest model.

### 3. **Deep Learning Pipeline**
   - Transformed JSON into images (RGB and Grayscale).
   - Trained CNN and Vision Transformer models for classification.

---

## Achievements

- **Published at ICDAM 2025** (Springer Lecture Notes in Networks and Systems)
- **ViT achieved 99.78% accuracy** (99.76% precision, recall and F1); CNN on RGB images 99.76%, CNN on grayscale 99.53%, Random Forest on tabular features 99.41%.

---


---

Built by [Satyam Kesharwani](https://www.satyamk.dev) · [LinkedIn](https://www.linkedin.com/in/stym01/) · [Engineering blog](https://www.satyamk.dev/blog)
