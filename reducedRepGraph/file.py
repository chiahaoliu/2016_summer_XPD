import os


def get_files(dir):
    """
    This function takes in a directory and returns a list of all tif files within
    :param dir: The user defined file path
    :type dir: str
    :return: A list of tif files
    """""

    if dir is None or len(dir) == 0:
        raise NotADirectoryError("Directory not specified")

    if dir[-1] != '/' or '\\':
        dir += '/'

    a = os.listdir(dir)
    file_list = [file for file in a if file.endswith('.tif') and not (file.endswith('.dark.tif') or file.endswith('.raw.tif'))]

    pic_list = []

    for file in file_list:
        pic_list.append(dir + file)

    return pic_list

