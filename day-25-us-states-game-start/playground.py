import os
import time

def get_files_with_mtime(folder):
    files = {}
    for root, _, filenames in os.walk(folder):
        for name in filenames:
            path = os.path.join(root, name)
            relative = os.path.relpath(path, folder)
            files[relative] = os.path.getmtime(path)
    return files

local = r"C:\Users\matti\pycharmprojects"
cloned = r"C:\Users\matti\Documents\100-Days-of-Code---The-Complete-Python-Pro-Bootcamp"

local_files = get_files_with_mtime(local)
cloned_files = get_files_with_mtime(cloned)

for file in sorted(set(local_files) | set(cloned_files)):
    l_time = local_files.get(file)
    c_time = cloned_files.get(file)

    if l_time and c_time:
        if l_time > c_time:
            print(f"NEWER in LOCAL:   {file}")
        #elif c_time > l_time:
         #   print(f"NEWER in CLONED:  {file}")
        else:
            pass  # same timestamp
    elif l_time:
        print(f"ONLY in LOCAL:    {file}")
    #else:
     #   print(f"ONLY in CLONED:   {file}")
