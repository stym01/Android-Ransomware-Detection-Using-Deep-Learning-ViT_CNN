# Deep Learning Algorithms on Images

This folder contains Jupyter notebooks implementing Convolutional Neural Networks (CNNs) for Android ransomware detection using image representations of behavioral data.

## Notebooks

### CNN_RGB_99.76_f1Score.ipynb
- **Purpose**: RGB CNN model for ransomware detection
- **Performance**: 99.76% F1 Score
- **Input**: RGB images (64x64 pixels) derived from JSON behavioral reports
- **Architecture**: Multi-layer CNN with convolution, pooling, and dense layers

### CNN_Grey_99.53_f1Score.ipynb  
- **Purpose**: Grayscale CNN model for ransomware detection
- **Performance**: 99.53% F1 Score
- **Input**: Grayscale images (64x64 pixels) derived from JSON behavioral reports
- **Architecture**: Similar CNN architecture optimized for single-channel input

## Dataset Structure

Before running these notebooks, ensure your dataset follows this structure:

```
dataset_root/
├── train/
│   ├── benign/          # Benign app images
│   └── malicious/       # Malicious app images  
├── val/
│   ├── benign/          # Validation benign images
│   └── malicious/       # Validation malicious images
└── test/
    ├── benign/          # Test benign images
    └── malicious/       # Test malicious images
```

## Setup Instructions

1. **Update Dataset Paths**: 
   - Replace `path/to/your/dataset` in the notebooks with your actual dataset path
   - Examples:
     ```python
     # For relative path:
     train_dataset = train.flow_from_directory('./data/processed_images/train/', ...)
     
     # For absolute path:
     train_dataset = train.flow_from_directory('/home/user/dataset/train/', ...)
     ```

2. **Install Dependencies**:
   ```bash
   pip install tensorflow matplotlib opencv-python numpy pandas scikit-learn
   ```

3. **Data Preparation**:
   - Convert JSON behavioral reports to images using the scripts in `../converting JSON to images/`
   - Split data into train/validation/test sets
   - Organize images according to the directory structure above

## Image Generation Process

The images used by these models are generated from CuckooDroid sandbox JSON reports:

1. **Feature Extraction**: Extract behavioral features from JSON reports
2. **Normalization**: Normalize feature values to 0-255 range  
3. **Image Creation**: Map features to RGB/Grayscale pixel values
4. **Size**: Generate 369x369 images, resized to 64x64 for training

## Model Architecture

Both models use similar CNN architectures:

- **Input Layer**: 64x64 images (RGB or Grayscale)
- **Convolutional Layers**: Multiple Conv2D layers with ReLU activation
- **Pooling Layers**: MaxPooling for dimension reduction
- **Dense Layers**: Fully connected layers for classification
- **Output**: Single sigmoid neuron for binary classification (benign/malicious)

## Training Configuration

- **Optimizer**: RMSprop with learning rate 0.001
- **Loss Function**: Binary crossentropy
- **Metrics**: Accuracy
- **Batch Size**: 3
- **Epochs**: 10
- **Input Size**: 64x64 pixels

## Performance Results

| Model | Input Type | Accuracy | F1 Score |
|-------|------------|----------|----------|
| CNN   | RGB        | 99.76%   | 99.76%   |
| CNN   | Grayscale  | 99.53%   | 99.53%   |

## Usage Notes

- The RGB model generally performs slightly better due to additional color channel information
- Both models achieve excellent performance for ransomware detection
- Ensure proper data preprocessing and augmentation for best results
- Models are trained on CuckooDroid behavioral analysis data converted to visual representations

## Related Files

- `../converting JSON to images/`: Scripts for converting JSON reports to images
- `../converting JSON to CSV data/`: Alternative CSV-based approach
- `../Applying Random Forest Classification on CSV/`: Traditional ML approach for comparison