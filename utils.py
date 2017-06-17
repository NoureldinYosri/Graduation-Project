import os,platform,shutil,re

def join_parent(directory, level=1):
    path = directory
    for i in range(level):
        path = os.path.join('..', path)
    return path

def join(dir, sub):
    return os.path.join(dir, sub)

def is_windows():
    return platform.system() == 'Windows'

def get_dirname(dirpath):
    return os.path.basename(dirpath)

def path_exists(path):
    return os.path.exists(path)

def make_dir(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
    print("creating:", path)
    os.makedirs(path)

def join_list(dir_list):
    return os.path.join(*(map(lambda x: normalize_dir(x), dir_list)))

def normalize_dir(path):
    return re.sub(r'[:*]', '-', path)
