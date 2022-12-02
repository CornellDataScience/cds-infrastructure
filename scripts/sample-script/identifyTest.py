import re
import os
import io

def writeTests(dirname):
    testfiles = searchDir(dirname)
    file = open("pytests.txt","w")
    for i in testfiles:
        file.write(i +"\n")

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
    prompted = input("Enter name of directory to search: ")
    print(writeTests(prompted))

if __name__ == "__main__":
    main()
