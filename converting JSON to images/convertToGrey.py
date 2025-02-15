import cv2
import os

# Specify the folder containing images
input_folder = r"C:\Users\satya\Desktop\ransom\cnn2\MORE\final_project\image_data_including_splitted_data\imageLast2\malicious"
output_folder = r"C:\Users\satya\Desktop\ransom\cnn2\MORE\final_project\image_data_including_splitted_data\greyImage\malicious"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Read the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        
        # Convert to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Save the grayscale image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, gray_img)

print("All images converted to grayscale and saved!")
