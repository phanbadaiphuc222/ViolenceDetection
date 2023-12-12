import os
from PIL import Image

def reverse_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            image = Image.open(input_path)
            reversed_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            reversed_image.save(output_path)
            print(f"Reversed {filename} and saved to {output_path}")
        except Exception as e:
            print(f"An error occurred while processing {filename}: {str(e)}")

input_folder = "C:/Users/OS/Desktop/temp/kicking"  # Replace with the actual input folder path
output_folder = "C:/Users/OS/Desktop/test2"  # Replace with the desired output folder path

reverse_images(input_folder, output_folder)
