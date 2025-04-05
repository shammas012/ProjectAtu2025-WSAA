import requests

actual_file_name = "sourcefile04.txt"  # name of original file
replacement_user_name = "shammas"  # name that replaces the word "andrew"

with open(actual_file_name, "r") as file:
    file = file.read()