from pathlib import Path
from datetime import datetime
import os
import glob

def remove(path):

    path = Path(path)
    files = [file for file in path.iterdir() if file.suffix == '.txt']

    sorted_list = sorted(files, key=os.path.getmtime, reverse=True)

    print(sorted_list)

    if len(sorted_list) > 3:
        for file in sorted_list[-1:-4:-1]:
            print(file)
            file.unlink()

def remove_os(path):

    list_files = []
    #files = [file for file in os.listdir(path) if os.path.splitext(file) == 'txt']

    #print(glob.glob(path))

    for file in glob.glob(path):

        _, ext = os.path.splitext(file)
        if ext == '.txt':
            list_files.append(os.path.abspath(file))

    sorted_list = sorted(list_files, key=os.path.getsize, reverse=True)

    print(sorted_list)

    #if len(sorted_list) > 3:
    #    for file in sorted_list[-1:-4:-1]:
    #        print(file)
            #os.remove(file)

remove_os('C:/Users/sam_m/OneDrive/Documents/*')




