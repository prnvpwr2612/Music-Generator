import os
import random

def delete_half_files(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Calculate the number of files to delete (half of the total files)
    num_files_to_delete = len(files) // 2
    
    # Randomly select files to delete
    files_to_delete = random.sample(files, num_files_to_delete)
    
    # Delete the selected files
    for file in files_to_delete:
        file_path = os.path.join(folder_path, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    # Specify the folder path
    folder_path = r"C:\Users\ppawa\Pranav\Study\Coding\Generative Deep Learning\Projects\Music-Generator\The_Magic_of_MIDI\MIDI"
    
    # Call the function to delete half of the files
    delete_half_files(folder_path)