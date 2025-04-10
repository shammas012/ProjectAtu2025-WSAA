import subprocess
import os

actual_file_name = "sourcefile04.txt"  # name of original file
existing_user_name = "Andrew"
replacement_user_name = "Shammas"  # name that replaces the word "andrew"

#The application was throwing fileNotFound exception eventhough both of the .py file and .txt file are in the same locations
#The below code gets the absolute path of the file
script_dir = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_dir, actual_file_name)

#Exception handling for reading file
try:
    #Readng the file
    with open(input_file_path, "r") as file:
        fileContent = file.read()
        file.close()
except FileNotFoundError:
    print(f"File not found: {input_file_path}")
    exit(1)
except Exception as e:
    print(f"Issues with reading file {input_file_path} : {e}")
    exit(1)

#Replace the word "Andrew" from the inputfile with developer's (my) own name. 
fileContent = fileContent.replace(existing_user_name, replacement_user_name)

#Exception handling for writing file
try:
    #Writing the file
    with open(input_file_path, "w") as file:
        file.write(fileContent)
        file.close()
except Exception as e:
    print(f"Issues with writing file {input_file_path} : {e}")
    exit(1)


#Exception handling for writing file
try:
    # Stage the file
    subprocess.run(["git", "add", input_file_path], check=True)

    status = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if status.returncode == 0:
        print("No staged changes to commit.")
        exit(0)

    subprocess.run(["git", "commit", "-m", f"Replaced text {existing_user_name} with text {replacement_user_name}"], check=True)
    subprocess.run(["git", "push"], check=True)

except Exception as e:
    print(f"Issues with committing changes to Github  : {e}")
    exit(1)
