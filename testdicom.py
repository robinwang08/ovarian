import os
import pydicom
from pydicom.data import get_testdata_files

filename = "./EE2ACC7C"

ds = pydicom.dcmread(filename)

print(str(ds))
