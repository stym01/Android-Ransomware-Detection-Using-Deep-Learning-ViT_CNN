import os
import cv2
import shutil
from sklearn.model_selection import train_test_split

# Define paths
benign_dir = r'C:\Users\satya\Desktop\ransom\cnn2\MORE\final_project\image_data_including_splitted_data\greyImage\benign'  # Replace with your benign folder path
malicious_dir = r'C:\Users\satya\Desktop\ransom\cnn2\MORE\final_project\image_data_including_splitted_data\greyImage\malicious'  # Replace with your malicious folder path
output_data_dir = r'C:\Users\satya\Desktop\ransom\cnn2\MORE\final_project\image_data_including_splitted_data\ProcessedGreyImage'  # Replace with desired output path

# Create output directories
if not os.path.exists(output_data_dir):
    os.makedirs(output_data_dir)
    for split in ['train', 'val', 'test']:
        for label in ['benign', 'malicious']:
            os.makedirs(os.path.join(output_data_dir, split, label))

# Access and sort benign images
print("Accessing benign images...")
benign_images = [os.path.join(benign_dir, f) for f in os.listdir(benign_dir)]
# benign_images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
print(f"Total benign images: {len(benign_images)}")

# Access and sort malicious images
print("Accessing malicious images...")
malicious_images = [os.path.join(malicious_dir, f) for f in os.listdir(malicious_dir)]
# malicious_images.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
print(f"Total malicious images: {len(malicious_images)}")

# Split data (70-20-10 split)
print("Splitting benign images...")
benign_train, benign_temp = train_test_split(benign_images, test_size=0.3, random_state=42)
benign_val, benign_test = train_test_split(benign_temp, test_size=0.33, random_state=42)

print("Splitting malicious images...")
malicious_train, malicious_temp = train_test_split(malicious_images, test_size=0.3, random_state=42)
malicious_val, malicious_test = train_test_split(malicious_temp, test_size=0.33, random_state=42)

# Function to process and save images using OpenCV
def process_and_save_images(file_list, destination, size=(369, 369)):
    print(f"Processing images for {destination}...")
    for file_path in file_list:
        # Read image using OpenCV
        img = cv2.imread(file_path)  # Load as grayscale
        if img is None:
            print(f"Warning: Unable to read image {file_path}")
            continue
        # Resize image
        img_resized = cv2.resize(img, size)
        # Save to destination
        file_name = os.path.basename(file_path)
        cv2.imwrite(os.path.join(destination, file_name), img_resized)
    print(f"Completed processing for {destination}.")

# Process and save images for each split
process_and_save_images(benign_train, os.path.join(output_data_dir, 'train', 'benign'))
process_and_save_images(malicious_train, os.path.join(output_data_dir, 'train', 'malicious'))

process_and_save_images(benign_val, os.path.join(output_data_dir, 'val', 'benign'))
process_and_save_images(malicious_val, os.path.join(output_data_dir, 'val', 'malicious'))

process_and_save_images(benign_test, os.path.join(output_data_dir, 'test', 'benign'))
process_and_save_images(malicious_test, os.path.join(output_data_dir, 'test', 'malicious'))

print("Data successfully split and processed!")
