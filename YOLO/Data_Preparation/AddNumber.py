import os

# Set the folder path where your files are located
folder_path = 'C:/Users/OS/Desktop/test2'

# Set the number to add to the current filenames
add_number = -220

# List all files in the folder
files = os.listdir(folder_path)

# Loop through all files in the folder and rename them
for old_name in files:
    # Split the file name and extension
    name, extension = os.path.splitext(old_name)
    
    # Add the number to the name part and keep the extension
    new_name = f"{int(name) + add_number}{extension}"
    
    # Rename the file
    os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
