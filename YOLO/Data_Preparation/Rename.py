import os

def rename_images(folder_path, start_number=1):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    if not image_files:
        print("No image files found in the folder.")
        return
    
    for index, filename in enumerate(image_files, start=start_number):
        file_extension = os.path.splitext(filename)[-1]
        new_filename = f"{index:d}{file_extension}"  # Format the index with leading zeros
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

folder_path = "C:/Users/OS/Desktop/test2"  # Replace with the actual path to your image folder
start_number = 14420 # Replace with the starting number you want

rename_images(folder_path, start_number)
