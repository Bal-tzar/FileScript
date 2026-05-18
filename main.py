from pathlib import Path

cleanUp = input("What directory would you like to clean up? ")
dir_path = Path(cleanUp)
print("--------- These are the files in ", cleanUp, "---------")
for item in dir_path.glob("*"):
    if item.is_file():
        print(item)
sortingChoice = input("Would you like to sort these files? yes/no   -")

if sortingChoice == 'yes':
    for files in dir_path.glob('*.txt'):
        folder_name = Path(cleanUp, 'texts/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.md'):
        folder_name = Path(cleanUp, 'texts/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.mp4'):
        folder_name = Path(cleanUp, 'movies/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.mp3'):
        folder_name = Path(cleanUp, 'music/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.py'):
        folder_name = Path(cleanUp, 'pythonProjects/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.png'):
        folder_name = Path(cleanUp, 'images/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.jpg'):
        folder_name = Path(cleanUp, 'images/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.pdf'):
        folder_name = Path(cleanUp, 'pdf/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.zip'):
        folder_name = Path(cleanUp, 'zip/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.deb'):
        folder_name = Path(cleanUp, 'misc/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    for files in dir_path.glob('*.gz'):
        folder_name = Path(cleanUp, 'misc/')
        folder_name.mkdir(parents=True, exist_ok=True)
        files.rename(dir_path / folder_name / files.name)

    print('Cleaned up in', dir_path)

else:
    print("Okay, I won't!")