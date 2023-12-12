import os
import shutil

source_folder = "C:/Users/OS/Desktop/temp/kicking"
destination_folder = "C:/Users/OS/Desktop/test2"

def copy_text_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(".txt"):  # Process only text files
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, file)
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} to {destination_path}")

def main():
    copy_text_files(source_folder, destination_folder)

if __name__ == "__main__":
    main()
