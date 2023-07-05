# lisaaniyat
# extracts dicoms from individual folders and puts them in the same folders
# author: ben lang, blang@ucsd.edu

import os
import sys
import time
import glob
import shutil


source = '/Volumes/circe/lisaaniyat/analysis/morpho_masking/data/'
destination = '/Volumes/circe/lisaaniyat/data_backup/avi/'
os.chdir(source)
allfolders = glob.glob(os.path.join(source, '*'))

all_avi = []
for folder in allfolders:
    os.chdir(folder)
    dicom_folders = glob.glob(os.path.join(os.getcwd(), '*'))
    for dicom in dicom_folders:
        if 'dicom' in dicom:
            os.chdir(dicom)
            run_folders = glob.glob(os.path.join(os.getcwd(), '*'))
            for run in run_folders:
                    os.chdir(run)
                    avi_files = glob.glob(os.path.join(os.getcwd(), '*'))
                    for avi in avi_files:
                        basenames = os.listdir()
                        for name in basenames:
                            if '.avi' in name:
                                os.rename(run + '/' + name, destination + '%s'%os.path.basename(folder) + '_' + name)

# all_folders = []
# for folder in allfolders:
#     if 'Run' in folder:
#         all_folders.append(folder)
#
# for folder in all_folders:
#     source = folder + '/'
#     allfiles = os.listdir(source)
#     for f in allfiles:
#         os.rename(source + f, destination + f)
