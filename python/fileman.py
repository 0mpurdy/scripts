import os

def extract_name(path, suffix):
    """Extracts the name of the file from the file path and removes the file extension"""
    filename = path.split('/')[-1]
    return filename[:-len(suffix)]


def get_filtered_files(folder, suffix, sort=True):
    """Get all files with a particular extension from a folder

    @param folder   Folder to search
    @param suffix   Filetype to find
    @param sort     Flag for alphabetically sorting results
    """
    files = [os.path.join(folder, item) for item in os.listdir(
        folder) if item.endswith(suffix)]
    if sort:
        files = sorted(files)
    return files

def filter_walk(directory, ignored_dirs, extension):
    """Walks through a directory and filters by file extension"""
    for path in get_files(directory, ignored_dirs):
        if path.endswith(extension):
            yield path

def get_files(directory, ignored_dirs=None):
    """Generator of file paths that are not in an ignored directory.

    By default ignores .git

    Uses some elements from:
    https://stackoverflow.com/questions/19859840/excluding-directories-in-os-walk
    """
    if ignored_dirs is None:
        ignored_dirs = ['.git']
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for ifile in files:
            yield os.path.join(root, ifile)
