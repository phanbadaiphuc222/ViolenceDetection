import os
import glob

# Replace 'source_folder' with the path to the folder containing text files
source_folder = 'C:/Users/OS/Desktop/train_data/labels/train'

# Replace 'output_folder' with the path to the folder where you want to save the result
output_folder = 'C:/Users/OS/Desktop/Gmail'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all text files in the source folder
text_files = glob.glob(os.path.join(source_folder, '*.txt'))

# Initialize an empty string to store the extracted text
extracted_text = ''

# Iterate through each text file and extract characters until the first space
for file_path in text_files:
    with open(file_path, 'r') as file:
        content = file.read()
        first_space_index = content.find(' ')
        if first_space_index != -1:
            extracted_text += f'File: {os.path.basename(file_path)}, Extracted Text: {content[:first_space_index]}\n'

# Define the path for the output text file
output_file_path = os.path.join(output_folder, 'extracted_text.txt')

# Write the extracted text to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(extracted_text)

print(f'Extracted text saved to {output_file_path}')
