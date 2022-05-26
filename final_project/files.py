
import os


def get_folder_files(folder):
    contents = os.listdir(folder)

    files = []

    for item in contents:
        path = folder + '/' + item

        if os.path.isdir(path):
            files.extend(get_folder_files(path))
        else:
            files.append(path)

    return files


def get_extension(file=""):
    parts = file.split(".")
    return parts.pop()


def is_png(file):
    return get_extension(file) == "png"


def get_file_name(file):
    parts = file.split("/")
    file_name = parts.pop()
    return file_name.split(".")[0]
