import requests
import os

actual_file_name = "sourcefile04.txt"  # name of original file
replacement_user_name = "shammas"  # name that replaces the word "andrew"
new_file_name = "assignment04Output.txt" # output should be saved here

#The application was throwing fileNotFound exception eventhough both of the .py file and .txt file are in the same locations
#Attempt to get the absolute location of the file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, actual_file_name)

try:
    with open(file_path, "r") as file:
        fileContent = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit(1)
except Exception as e:
    print(f"Issues with reading file {file_path} : {e}")
    exit(1)