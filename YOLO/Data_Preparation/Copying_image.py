import os
import shutil

def copy_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    for filename in image_files:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        try:
            shutil.copy2(source_path, destination_path)  # Use shutil.copy() for older versions of Python
            print(f"Copied {filename} to {destination_path}")
        except Exception as e:
            print(f"An error occurred while copying {filename}: {str(e)}")

source_folder = "C:/Users/OS/Desktop/temp/kicking"  # Replace with the source folder path
destination_folder = "C:/Users/OS/Desktop/test2"  # Replace with the destination folder path

copy_images(source_folder, destination_folder)
