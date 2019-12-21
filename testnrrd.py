import numpy as np
import nrrd


# Read the data back from file
readdata, header = nrrd.read('/media/user1/my4TB/robin/ovarian/ovarian_data/raw/9033903-1/T1POST/imagingVolume.nrrd')
print(readdata.shape)
print(header)