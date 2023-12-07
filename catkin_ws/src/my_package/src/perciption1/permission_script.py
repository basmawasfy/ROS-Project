import os

file_path = 'images/tree.jpg'

# Check if the file exists
if os.path.exists(file_path):
    # Get the file permissions
    permissions = os.stat(file_path).st_mode

    # Check if the file is readable
    if os.access(file_path, os.R_OK):
        print(f"The file '{file_path}' is readable.")
    else:
        print(f"Warning: The file '{file_path}' is not readable.")

    # Check if the file is writable
    if os.access(file_path, os.W_OK):
        print(f"The file '{file_path}' is writable.")
    else:
        print(f"Warning: The file '{file_path}' is not writable.")

    # Check if the file is executable
    if os.access(file_path, os.X_OK):
        print(f"The file '{file_path}' is executable.")
    else:
        print(f"Warning: The file '{file_path}' is not executable.")
else:
    print(f"Error: The file '{file_path}' does not exist.")