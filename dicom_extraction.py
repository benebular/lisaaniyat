# lisaaniyat
# extracts dicoms from individual folders and puts them in the same folders
# author: ben lang, blang@ucsd.edu

import sklearn
import numpy as np
import pandas as pd
import os
import sys
import time
import glob


source = '/Volumes/circe/rtMRI/lisaaniyat/Sub0271_LP_Vocal_Y0368/Sub0271_dicom'
os.chdir(source)

allfolders = glob.glob(os.path.join(source, '*'))

all_folders = []
for folder in allfolders:
    if 'Run' in folder:
        all_folders.append(folder)

destination = '/Volumes/circe/rtMRI/lisaaniyat/Sub0271_LP_Vocal_Y0368/Sub0271_dicom/all_dicom/'

for folder in all_folders:
    source = folder + '/'
    allfiles = os.listdir(source)
    for f in allfiles:
        os.rename(source + f, destination + f)
