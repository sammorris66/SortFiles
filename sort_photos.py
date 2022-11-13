import os
from datetime import datetime
import shutil

# Create Sub Directories with the year as a date
def create_folders(path='C:\photos'):

    os.chdir(path)
    photos = os.listdir()
    dist_years = []

    for photo in photos:

        if os.path.isdir(photo) is True:
            dist_years.append(photo)
        else:
            time = os.stat(photo).st_mtime
            year = datetime.fromtimestamp(time).year
            if year not in dist_years:
                dist_years.append(year)

    unique_years = set(dist_years)
    print(unique_years)

    for dy in unique_years:

        try:
            os.makedirs(str(dy))
        except (FileExistsError, PermissionError) as e:
            print(e)

# Move files to sub-dictories according to the year they were modified
def move_photos_folder(path='C:\photos'):

    os.chdir(path)
    photos = os.listdir()

    list_folders = {folder for folder in os.listdir() if os.path.isdir(folder)}
    print(list_folders)

    for photo in photos:
        if os.path.isfile(photo):
            time = os.stat(photo).st_mtime
            year = datetime.fromtimestamp(time).year
            src = os.path.join(os.getcwd(), photo)

            for folder in list_folders:
                if folder == str(year):
                    dst = os.path.join(os.getcwd(), folder)
                    shutil.move(src, dst)


# Re-name files
def rename_photos(path='C:\photos'):

    os.chdir(path)

    for root, dirpath, filename in os.walk(os.getcwd()):

        for index, file in enumerate(filename):
            print(index, file)
            new_name = '{}_Family_Time1.jpg'.format(index)
            src = os.path.join(root, file)
            dst = os.path.join(root, new_name)
            try:
                os.rename(src, dst)
            except FileExistsError as e:
                print(e)


# Move files from the source folder to the photos folder
def move_to_photos_folder(from_path, to_path='C:/photos'):


    os.chdir(from_path)
    dst_path = to_path

    for root, dirpath, filename in os.walk(os.getcwd()):
        print(f'{root}')
        for file in filename:
            print(f'{root}')
            src = os.path.join(root, file)
            try:
                shutil.move(src, dst_path)
            except:
                print(f'{file} had a problem')


move_to_photos_folder('C:/Users/sam_m/OneDrive/Pictures')
create_folders()
move_photos_folder()
rename_photos()





