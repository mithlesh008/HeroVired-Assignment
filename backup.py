import shutil
import sys
import os

source = sys.argv[1]
dest = sys.argv[2]

def check_source():
    if os.path.exists(source):
        return True
    
def check_dest():
    if os.path.exists(dest):
        return True
    
def backup():
    if check_dest() and check_source():
        shutil.copy(source,dest)
        print(f"backup is done from {source} to {dest}")
    else:
        print(f"{source} or {dest} not exist")

backup()