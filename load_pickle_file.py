from dependencies import *

parent_directory = "C:\\Users\\Soheil\\Desktop\\Experiments\\Data\\"
file_name = "file_name.pickle"
file_address = parent_directory + file_name

objects = []
with (open(file_address, "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break

    print(objects)