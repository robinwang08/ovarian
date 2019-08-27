import nrrd
import numpy as np
from glob import glob
import pathlib
import os.path


def dice_score(seg_1, seg_2):
    return np.sum(seg_1[seg_2==1])*2.0 / (np.sum(seg_1) + np.sum(seg_2))


def calc():
    avgzzzj = 0
    avgrawzz = 0
    avgrawzj = 0
    count = 0

    patho = '/media/user1/my4TB/robin/ovarian/ovarian_data'
    baseDir = os.path.normpath(patho)
    files1 = glob(baseDir + '/zj/*/T1POST/segMask_tumor.nrrd')

    for file in files1:
        count = count + 1
        filePath, fileName = os.path.split(file)
        a = filePath.split('/')

        zzstartPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/zz/'
        zznePath = zzstartPath + '/' + a[8]
        zzzPathFile = zzstartPath + '/T1POST' + fileName

        rawstartPath = '/media/user1/my4TB/robin/ovarian/ovarian_data/raw/'
        rawnePath = rawstartPath + '/' + a[8]
        rawwnePathFile = rawnePath + '/T1POST' + fileName


        zj_nrrd = nrrd.read(file)
        zjdata = zj_nrrd[0]

        zz_nrrd = nrrd.read(zzzPathFile)
        zzdata = zz_nrrd[0]

        raw_nrrd = nrrd.read(rawwnePathFile)
        rawdata = raw_nrrd[0]

        avgzzzj = avgzzzj + dice_score(zzdata, zjdata)
        avgrawzz = avgrawzz + dice_score(rawdata, zzdata)
        avgrawzj = avgrawzj + dice_score(rawdata, zjdata)

        print('done with ' + file)

    a = avgzzzj / count
    b = avgrawzj / count
    c = avgrawzz / count

    print('zz-zj: ' + str(a))
    print('raw-zj: ' + str(b))
    print('raw-zz: ' + str(c))