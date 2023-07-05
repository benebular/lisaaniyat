## lisaaniyat plotting
# author: Ben Lang, blang@ucsd.edu, ben.lang@nyu.edu


import numpy as np
import pandas as pd
import time
import seaborn as sns
import ptitprince as pt
import os
import os.path as op
import sys
import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import transforms
import string
np.set_printoptions(threshold=sys.maxsize)

# set up directory and read in csv
dir = '/Volumes/circe/lisaaniyat/data_backup/vt_points/'
fig_dir = '/Volumes/circe/lisaaniyat/data_backup/figs/'
# fig_dir = '/Users/bcl/Library/CloudStorage/GoogleDrive-bcl267@nyu.edu/My Drive/Nellab/rtMRI Arabic/lsa2024/data/figs'
os.chdir(dir)

Y0365_voiced_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_4_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_5_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_6_pts']
Y0373_voiced_pts_list = ['Sub0269_Lp_Vocal_Y0373_lisaaniyat_4_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_5_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_6_pts']
Y0368_voiced_pts_list = ['Sub0271_Lp_Vocal_Y0368_lisaaniyat_4_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_5_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_6_pts']
Y0365_voiceless_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_7_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_8_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_9_pts']
Y0373_voiceless_pts_list = ['Sub0269_Lp_Vocal_Y0373_lisaaniyat_8_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_9_pts']
Y0368_voiceless_pts_list = ['Sub0271_Lp_Vocal_Y0368_lisaaniyat_7_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_8_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_9_pts']					

base = plt.gca().transData
rot = transforms.Affine2D().rotate_deg(90)


fig, ax = plt.subplots(1,3)
fig.suptitle('Vocal Tract Contours for /ʕ/ and /ħ/ in Modern Standard Arabic', fontsize = 20)

for pts in Y0365_voiced_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[0].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
	ax[0].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

for pts in Y0365_voiceless_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[0].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
	ax[0].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

for pts in Y0373_voiced_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[1].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
	ax[1].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

for pts in Y0373_voiceless_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[1].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
	ax[1].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

for pts in Y0368_voiced_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[2].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
	ax[2].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

for pts in Y0368_voiceless_pts_list:
	pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
	pts = pd.read_csv(pts_fname)
	# pts['rt_1'] = -pts['rt_1']
	# pts['lf_1'] = -pts['lf_1']
	ax[2].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
	ax[2].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

# plt.gca().invert_yaxis()
ax[0].set_title('Tunisian Speaker', fontsize = 20)
ax[1].set_title('Egyptian Speaker', fontsize = 20)
ax[2].set_title('Palestinian Speaker', fontsize = 20)

labels = ['/ʕ/', '/ħ/']

from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color='#984ea3', lw=4),
                Line2D([0], [0], color='#ff7f00', lw=4)]
# ax[0].get_legend().remove()
# ax[1].get_legend().remove()    
ax[0].legend(custom_lines, labels)
ax[1].legend(custom_lines, labels)
ax[2].legend(custom_lines, labels)
ax[0].set_xlabel('Distance (mm)', fontsize = 20)
ax[1].set_xlabel('Distance (mm)', fontsize = 20)
ax[2].set_xlabel('Distance (mm)', fontsize = 20)
ax[0].set_ylabel('Distance (mm)', fontsize = 20)
ax[1].set_ylabel('Distance (mm)', fontsize = 20)
ax[2].set_ylabel('Distance (mm)', fontsize = 20)

plt.show()
