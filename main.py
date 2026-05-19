from pathlib import Path
import json

with(open('config.json')) as config_file:
    data = json.load(config_file)

target_directory = input("Which directory would you like to clean up? ")
dir_path = Path(target_directory)
print("--------- These are the unsorted files in ", target_directory, "---------")
for item in dir_path.glob("*"):
    if item.is_file():
        print(item)


sorting_choice = input("Would you like to sort these files? yes/no:   ")


if sorting_choice == 'yes':
    for files in dir_path.glob('*'):
        if files.is_file():
            extension = files.suffix
            if extension in data:
                folder_name = data[extension]
                destination = Path(target_directory, folder_name)
                destination.mkdir(parents=True, exist_ok=True)
                files.rename(destination / files.name)
    print('Cleaned up in', dir_path)

else:
    print("Okay, I won't!")