import requests
import os

actual_file_name = "sourcefile04.txt"  # name of original file
replacement_user_name = "shammas"  # name that replaces the word "andrew"

#The application was throwing fileNotFound exception eventhough both of the .py file and .txt file are in the same locations
#Attempt to get the absolute location of the file
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, actual_file_name)

with open(file_path, "r") as file:
    fileContent = file.read()