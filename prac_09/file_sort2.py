import shutil
import os

print("Current directory is", os.getcwd())
os.chdir('FilesToSort')
print("Current directory is", os.getcwd())
print(os.listdir('.'))

extensions = []
dir_names = []
extension_directory = {}
for filename in os.listdir('.'):
    (name, extension) = os.path.splitext(filename)
    print(extension)

    if extension not in extensions:
        extensions.append(extension)
        dir_name = input("What category would you like to sort {} files into?".format(extension.strip(".")))
        extension_directory[extension] = dir_name
        if dir_name not in dir_names:
            dir_names.append(dir_name)
            os.mkdir(dir_name)
        shutil.move(filename, dir_name)
    elif extension in extensions:
        dir_name = extension_directory[extension]
        shutil.move(filename, dir_name)
