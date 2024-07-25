import os
import shutil
import sys

def copy_files(input_folder, output_folder, folder_names=None):
    if folder_names is None:
        folder_names = []
    
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isdir(item_path):
            copy_files(item_path, output_folder, folder_names + [item])
        else:
            filename, extension = os.path.splitext(item)
            new_filename = filename + ',,' + ',,'.join(folder_names) + extension
            output_path = os.path.join(output_folder, new_filename)
            shutil.copy(item_path, output_path)

if __name__ == "__main__":
    # Check if two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Call the function to copy files
    copy_files(input_folder, output_folder)
    print("Files copied successfully!")
