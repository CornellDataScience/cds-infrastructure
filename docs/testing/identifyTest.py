import re
import os


def searchDir(dirname):
    test_files = []
    for pathname in os.listdir(dirname):
        entirepath = dirname+"/"+pathname
        # print("current pathname "+pathname)
        if os.path.isdir(dirname+"/"+pathname):
            # print("looking through directory")
            test_files = test_files + searchDir(entirepath)
        else:
            if identifyTest(dirname+"/"+pathname):
                # print("current valid test"+entirepath)
                test_files = test_files + [pathname]
    return test_files


def identifyTest(filename):
    if re.search('test_', file_to_string(filename)):
        return True
    return False


def file_to_string(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data
