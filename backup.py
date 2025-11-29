import shutil
import sys
import os
from datetime import datetime

if len(sys.argv) != 3:
    print("""Error: Please enter valid Arguments
          Either Source or Destination is missing
          Make sure source and destination should be Directory""")
    sys.exit(1)

source = sys.argv[1]
dest = sys.argv[2]

def empty_dir():
    try:
        if not os.listdir(source):
            print(f"Error: {source} is Empty Directory")
            sys.exit(1)
    except Exception as e:
        print(f"Error: Your Source Directory may be empty or not exist : {e}")

def check_source_dest():
    if not os.path.isdir(source) and not os.path.isdir(dest):
        print(f'Error source: "{source}" is not valid directory')
        print(f'Error destination: "{dest}" is not valid directory')
    elif not os.path.isdir(source) or not os.path.exists(source):
        print(f'Error source: "{source}" is not valid directory')
        sys.exit(1)
    elif not os.path.isdir(dest) or  not os.path.exists(dest):
        print(f'Error destination: "{dest}" is not valid directory')
        sys.exit(1)

    
def backup():
    files_copied = 0
    check_source_dest()
    empty_dir()
    try:
        for i in os.listdir(source):
            source_path = os.path.join(source, i)
            print(f"""Here is the list of the files from source: 
              {source_path}""")
            if os.path.isfile(source_path):
                dest_path = os.path.join(dest, i)
                print(f"""Checking if file already exists at {source}: 
                    {dest_path}""")
                if os.path.exists(dest_path):
                    print(f"File {i} Already Exists at Destination")
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_filename = f"{i}-{timestamp}"
                    # print(new_filename)
                    dest_path = os.path.join(dest, new_filename)
                    print(f"New File name is {dest_path}")
                try:
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied: {i} with newname → {dest_path}")
                    files_copied = files_copied + 1
                except Exception as e:
                    print(f"Error copying file '{i}': {e}")
    except Exception as e:
        print(e)

    if files_copied > 0:
        print(f"\nBackup is done from {source} to {dest} and Total number of {files_copied} files copied")
    else:
        print("\nNo files were backed up.")

backup()