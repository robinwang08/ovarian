from glob import glob
import pathlib
import os.path
from os import path
import shutil


patho = 'E:/Research/need-to-align_completed'
baseDir = os.path.normpath(patho)
files = glob(baseDir + '/*/label.nii')

for file in files:
    filePath, fileName = os.path.split(file)
    a = filePath.split('\\')


    nePath = 'E:/Research/stroke/' + a[3]
    newPath = nePath + '/' + fileName

    if not os.path.isdir(nePath):
        os.mkdir(nePath)

    if not os.path.isdir(nePath):
        os.mkdir(nePath)

    shutil.move(file, newPath)