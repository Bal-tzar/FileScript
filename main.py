from pathlib import Path
import json

with(open('config.json')) as config_file:
    data = json.load(config_file)

cleanUp = input("Which directory would you like to clean up? ")
dir_path = Path(cleanUp)
print("--------- These are the unsorted files in ", cleanUp, "---------")
for item in dir_path.glob("*"):
    if item.is_file():
        print(item)
sortingChoice = input("Would you like to sort these files? yes/no:   ")
if sortingChoice == 'yes':
    for files in dir_path.glob('*'):
        if files.is_file():
            extension = files.suffix
            if extension in data:
                folder_name = data[extension]
                destination = Path(cleanUp, folder_name)
                destination.mkdir(parents=True, exist_ok=True)
                files.rename(dir_path / folder_name / files.name)
    print('Cleaned up in', dir_path)

else:
    print("Okay, I won't!")