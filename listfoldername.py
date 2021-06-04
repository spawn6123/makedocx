from os import listdir
from os.path import isdir, join
from os import walk


def listfoldername(findpath):
    """
    回傳資料匣名稱
    """
    foldernames = []
    fs = listdir(findpath)
    for f in fs:
        fullpath = join(findpath, f)
        if isdir(fullpath):
            foldernames.append(fullpath)

    return foldernames


def getfiles(despath):
    """
    回傳陣列檔案
    """
    outfilepath = []
    for root, dirs, files in walk(despath):
        for f in files:
            fullfilepath = join(despath, f)
            outfilepath.append(fullfilepath)
        return outfilepath
