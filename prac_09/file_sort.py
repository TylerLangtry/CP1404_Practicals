import shutil
import os

print("Current directory is", os.getcwd())
os.chdir('FilesToSort')
print("Current directory is", os.getcwd())
print(os.listdir('.'))

extensions = []
for filename in os.listdir('.'):
    (name, extension) = os.path.splitext(filename)
    print(extension)

    if extension not in extensions:
        extensions.append(extension)
        dir_name = extension.strip(".")
        os.mkdir(dir_name)
        shutil.move(filename, dir_name)
    elif extension in extensions:
        dir_name = extension.strip(".")
        shutil.move(filename, dir_name)



print(extensions)
