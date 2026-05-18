from pathlib import Path

dir_path = Path('/home/ottodm/Downloads/')

for files in dir_path.glob('*.txt'):
    folder_name = Path('/home/ottodm/Downloads/texts/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.md'):
    folder_name = Path('/home/ottodm/Downloads/texts/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.mp4'):
    folder_name = Path('/home/ottodm/Downloads/movies/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.mp3'):
    folder_name = Path('/home/ottodm/Downloads/music/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.py'):
    folder_name = Path('/home/ottodm/Downloads/pythonProjects/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.png'):
    folder_name = Path('/home/ottodm/Downloads/images/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.jpg'):
    folder_name = Path('/home/ottodm/Downloads/images/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.pdf'):
    folder_name = Path('/home/ottodm/Downloads/pdf/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

for files in dir_path.glob('*.zip'):
    folder_name = Path('/home/ottodm/Downloads/zip/')
    folder_name.mkdir(parents=True, exist_ok=True)
    files.rename(dir_path / folder_name / files.name)

print('Cleaned up in', dir_path)