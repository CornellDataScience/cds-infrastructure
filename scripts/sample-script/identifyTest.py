import re
import os
import io
import yaml


def writeTests(dirname):
    testfiles = searchDir(dirname)
    file = open("pytests.txt","w")
    for i in range(0, len(testfiles)):
      #if i < len(testfiles) - 1:
      file.write(testfiles[i] +"\n")
      #else:
      #  file.write(testfiles[i])

def searchDir(dirname):
    test_files =[]
    for pathname in os.listdir(dirname):
        entirepath = dirname+"/"+pathname
        # print("current pathname "+pathname)
        if os.path.isdir(dirname+"/"+pathname):
            # print("looking through directory")
            test_files = test_files+ searchDir(entirepath)
        else:
            if identifyTest(dirname+"/"+pathname):
                # print("current valid test"+entirepath)
                pathname = dirname+"/"+pathname
                test_files = test_files +[pathname]
    return test_files

def identifyTest(filename):
    if re.search('test_', file_to_string(filename)):
        return True
    return False

def file_to_string(filename):
    with io.open(filename, encoding="utf8", errors='ignore') as file:
        data = file.read()
    return data

def main():
    #prompted = input("Enter name of directory to search: ")
  with open('../../config.yml') as info:
    meta = yaml.load(info)
    prompted = "../../" + meta["REPOSITORY_NAME"]
    print(writeTests(prompted))

if __name__ == "__main__":
    main()