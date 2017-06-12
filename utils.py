import os,platform

def join_parent(directory, level=1):
    path = directory
    for i in range(level):
        path = os.path.join('..', path)
    return path

def join(dir, sub):
    return os.path.join(dir, sub)

def is_windows():
    return platform.system() == 'Windows'