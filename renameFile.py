#coding=gbk
import os
import random
import re


if __name__ == '__main__':
    path='./Train'
    for root, dirs, files in os.walk(path):
        for file in files:
            fileName = os.path.basename(file)
            r = re.compile(r'[\u4e00-\u9fa5]+')
            mat = r.findall(fileName)
            if mat:
                newPrefName = str(random.randint(0,2))
                newName = re.sub(r, "_"+newPrefName, fileName)
                newName = re.sub(re.compile(r'\s'), '', newName)
                newName = re.sub(re.compile(r'-'), '', newName)
                oldName = os.path.join(root, file)
                newName = os.path.join(root, newName)
                os.rename(oldName, newName)
