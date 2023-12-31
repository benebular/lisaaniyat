## lisaaniyat plotting
# author: Ben Lang, blang@ucsd.edu, ben.lang@nyu.edu


import numpy as np
import pandas as pd
import time
import seaborn as sns
# import ptitprince as pt
import os
import os.path as op
import sys
# import scipy.stats as stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib.lines import Line2D
from matplotlib import transforms
import string
# np.set_printoptions(threshold=sys.maxsize)

# set up directory and read in csv
dir = '/Volumes/hecate/lisaaniyat/data_backup/vt_points/'
fig_dir = '/Volumes/hecate/lisaaniyat/data_backup/figs/'
# fig_dir = '/Users/bcl/Library/CloudStorage/GoogleDrive-bcl267@nyu.edu/My Drive/Nellab/rtMRI Arabic/lsa2024/data/figs'
os.chdir(dir)


# lary_fric_pts_list = ['Subject_0464_Lp_Vocal_Y0412_lisaaniyat_2_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_4_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_6_pts',
#                             'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_8_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_10_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_2_pts',
#                             'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_4_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_6_pts','Subject_0466_Lp_Vocal_Y0413_lisaaniyat_8_pts',
#                             'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_10_pts']            
# lary_stop_pts_list = ['Subject_0464_Lp_Vocal_Y0412_lisaaniyat_1_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_3_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_5_pts',
#                             'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_7_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_9_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_1_pts',
#                             'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_3_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_5_pts','Subject_0466_Lp_Vocal_Y0413_lisaaniyat_7_pts',
#                             'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_9_pts']

##### Y0368 ####### Palestinian
phary_fric_pts_list = ['Sub0271_LP_Vocal_Y0368_lisaaniyat_8_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_11_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_14_pts',
                            'Sub0271_LP_Vocal_Y0368_lisaaniyat_20_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_23_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_32_pts',
                            'Sub0271_LP_Vocal_Y0368_lisaaniyat_38_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_44_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_50_pts']                 
phary_approx_pts_list = ['Sub0271_LP_Vocal_Y0368_lisaaniyat_2_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_5_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_17_pts',
                            'Sub0271_LP_Vocal_Y0368_lisaaniyat_26_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_29_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_35_pts',
                            'Sub0271_LP_Vocal_Y0368_lisaaniyat_41_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_47_pts', 'Sub0271_LP_Vocal_Y0368_lisaaniyat_53_pts']                 


##### Y0365 ####### Tunisian
phary_fric_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_8_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_11_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_14_pts',
                            'Sub0256_Lp_Vocal_Y0365_lisaaniyat_20_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_23_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_32_pts',
                            'Sub0256_Lp_Vocal_Y0365_lisaaniyat_38_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_44_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_50_pts']                 
phary_approx_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_2_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_5_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_17_pts',
                            'Sub0256_Lp_Vocal_Y0365_lisaaniyat_26_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_29_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_35_pts',
                            'Sub0256_Lp_Vocal_Y0365_lisaaniyat_41_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_47_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_53_pts']                 

# # Function to scale columns to a range between 0 and 100
# def scale_to_proportional(df, columns):
#     for col in columns:
#         df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min()) * 100
#     return df

# # List of columns to be scaled
# columns_to_scale = ['rt_1', 'rt_2', 'lf_1', 'lf_2']

# Define colors for each list
colors = {
    'lary_fric': '#1b9e77',   # Green-like color
    'lary_stop': '#e7298a',   # Pink-like color
    'phary_fric': '#d95f02',  # Orange-like color
    'phary_approx': '#7570b3' # Blue-like color
}

# Pair each list with its corresponding name
list_names = ['phary_fric', 'phary_approx']
lists = [phary_fric_pts_list, phary_approx_pts_list]

# set up fig
fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle('Vocal Tract Contours for Pharyngeal /ħ ʕ/', fontsize=28)

# Iterate over the list names and the corresponding lists
for i, (list_name, pts_list) in enumerate(zip(list_names, lists)):
    for pts in pts_list:
        pts_fname = os.path.join(dir, f'{pts}.csv')
        print(f"Reading file: {pts_fname}")  # Debugging line
        pts_data = pd.read_csv(pts_fname)
        print(pts_data.head())  # Debugging line to check if data is read correctly
        # scaled_df = scale_to_proportional(pts_data,columns_to_scale)
        # ax = axs[i // 2, i % 2]  # Adjust indexing based on your subplot arrangement
        # Ensure you are using the correct column names from your CSV files
        ax.plot(pts_data['rt_1'], pts_data['rt_2'], color=colors[list_name])
        ax.plot(pts_data['lf_1'], pts_data['lf_2'], color=colors[list_name])


        # Set y-axis label only for the first plot
        if i == 0:
            ax.set_ylabel('Distance (mm)', fontsize=16)

        # Set x-axis label for all plots (or adjust as needed)
        ax.set_xlabel('Distance (mm)', fontsize=16)
ax.invert_yaxis()  # Inverting the y-axis

# Create custom legend handles
legend_handles = [
    Line2D([0], [0], color=colors['phary_fric'], lw=3, label='ħ'),
    Line2D([0], [0], color=colors['phary_approx'], lw=3, label='ʕ')
]

# Add the custom legend to the plot
# ax.legend(handles=legend_handles)
ax.legend(handles=legend_handles, fontsize=18, handlelength=2, labelspacing=1.2)


plt.title('Speaker 2 (Tunisian)', fontsize=18)


# Show plot
plt.show()

##### Y0413 #### Levantine
lary_fric_pts_list = ['Subject_0466_Lp_Vocal_Y0413_lisaaniyat_2_pts',
                            'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_4_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_6_pts','Subject_0466_Lp_Vocal_Y0413_lisaaniyat_8_pts',
                            'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_10_pts']            
lary_stop_pts_list = ['Subject_0466_Lp_Vocal_Y0413_lisaaniyat_1_pts',
                            'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_3_pts', 'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_5_pts','Subject_0466_Lp_Vocal_Y0413_lisaaniyat_7_pts',
                            'Subject_0466_Lp_Vocal_Y0413_lisaaniyat_9_pts']

###### Y0412 ####### Moroccan
lary_fric_pts_list = ['Subject_0464_Lp_Vocal_Y0412_lisaaniyat_2_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_4_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_6_pts',
                            'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_8_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_10_pts']            
lary_stop_pts_list = ['Subject_0464_Lp_Vocal_Y0412_lisaaniyat_1_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_3_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_5_pts',
                            'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_7_pts', 'Subject_0464_Lp_Vocal_Y0412_lisaaniyat_9_pts']

# Pair each list with its corresponding name
list_names = ['lary_fric', 'lary_stop']
lists = [lary_fric_pts_list, lary_stop_pts_list]

# set up fig
fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle('Vocal Tract Contours for Laryngeal /h ʔ/', fontsize=28)


# Iterate over the list names and the corresponding lists
for i, (list_name, pts_list) in enumerate(zip(list_names, lists)):
    for pts in pts_list:
        pts_fname = os.path.join(dir, f'{pts}.csv')
        print(f"Reading file: {pts_fname}")  # Debugging line
        pts_data = pd.read_csv(pts_fname)
        print(pts_data.head())  # Debugging line to check if data is read correctly
        # scaled_df = scale_to_proportional(pts_data,columns_to_scale)
        # ax = axs[i // 2, i % 2]  # Adjust indexing based on your subplot arrangement
        # Ensure you are using the correct column names from your CSV files
        ax.plot(pts_data['rt_1'], pts_data['rt_2'], color=colors[list_name])
        ax.plot(pts_data['lf_1'], pts_data['lf_2'], color=colors[list_name])

        # ax[i].invert_xaxis()  # Inverting the y-axis

        # Set y-axis label only for the first plot
        if i == 0:
            ax.set_ylabel('Distance (mm)', fontsize=16)

        # Set x-axis label for all plots (or adjust as needed)
        ax.set_xlabel('Distance (mm)', fontsize=16)
ax.invert_yaxis()  # Inverting the y-axis

# Create custom legend handles
legend_handles = [
    Line2D([0], [0], color=colors['lary_fric'], lw=2, label='h'),
    Line2D([0], [0], color=colors['lary_stop'], lw=2, label='ʔ')
]

# Add the custom legend to the plot
# ax.legend(handles=legend_handles)
ax.legend(handles=legend_handles, fontsize=18, handlelength=2, labelspacing=1.2)

plt.title('Speaker 4 (Moroccan)', fontsize=18)

# Show plot
plt.show()



#### four conditions ######

# Pair each list with its corresponding name
list_names = ['lary_fric', 'lary_stop', 'phary_fric', 'phary_approx']
lists = [lary_fric_pts_list, lary_stop_pts_list, phary_fric_pts_list, phary_approx_pts_list]

# Create custom legend handles
legend_handles = [
    Line2D([0], [0], color=colors['lary_fric'], lw=2, label='h'),
    Line2D([0], [0], color=colors['lary_stop'], lw=2, label='ʔ'),
    Line2D([0], [0], color=colors['phary_fric'], lw=2, label='ħ'),
    Line2D([0], [0], color=colors['phary_approx'], lw=2, label='ʕ')
]



#### archive for one base graph with two conditions #####
# Define colors for each list
colors = {
    'lary_fric': '#1b9e77',   # Green-like color
    'lary_stop': '#e7298a',   # Pink-like color
    'phary_fric': '#d95f02',  # Orange-like color
    'phary_approx': '#7570b3' # Blue-like color
}

# Pair each list with its corresponding name
list_names = ['phary_fric', 'phary_approx']
lists = [phary_fric_pts_list, phary_approx_pts_list]

# set up fig
fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle('Vocal Tract Contours for Pharyngeal /ħ ʕ/', fontsize=28)

# Iterate over the list names and the corresponding lists
for i, (list_name, pts_list) in enumerate(zip(list_names, lists)):
    for pts in pts_list:
        pts_fname = os.path.join(dir, f'{pts}.csv')
        print(f"Reading file: {pts_fname}")  # Debugging line
        pts_data = pd.read_csv(pts_fname)
        print(pts_data.head())  # Debugging line to check if data is read correctly
        # scaled_df = scale_to_proportional(pts_data,columns_to_scale)
        # ax = axs[i // 2, i % 2]  # Adjust indexing based on your subplot arrangement
        # Ensure you are using the correct column names from your CSV files
        ax.plot(pts_data['rt_1'], pts_data['rt_2'], color=colors[list_name])
        ax.plot(pts_data['lf_1'], pts_data['lf_2'], color=colors[list_name])


        # Set y-axis label only for the first plot
        if i == 0:
            ax.set_ylabel('Distance (mm)', fontsize=16)

        # Set x-axis label for all plots (or adjust as needed)
        ax.set_xlabel('Distance (mm)', fontsize=16)
ax.invert_yaxis()  # Inverting the y-axis

# Create custom legend handles
legend_handles = [
    Line2D([0], [0], color=colors['phary_fric'], lw=3, label='ħ', fontsize=16),
    Line2D([0], [0], color=colors['phary_approx'], lw=3, label='ʕ', fontsize=16)
]

# Add the custom legend to the plot
ax.legend(handles=legend_handles)

plt.title('Speaker 1 (Palestinian)', fontsize=18)


# Show plot
plt.show()


# # Plotting for each list of points
# for list_name, pts_list in zip(list_names, lists):
#     for pts in pts_list:
#         pts_fname = os.path.join(dir, f'{pts}.csv')
#         pts_data = pd.read_csv(pts_fname)
#         axis.plot(pts_data['rt_1'], pts_data['rt_2'], color=colors[list_name])
#         axis.plot(pts_data['lf_1'], pts_data['lf_2'], color=colors[list_name])
#     axis.invert_yaxis()  # Inverting the y-axis
#     # axis.invert_xaxis()  # Inverting the x-axis

# plt.show()

# Y0365_voiced_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_4_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_5_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_6_pts']
# Y0373_voiced_pts_list = ['Sub0269_Lp_Vocal_Y0373_lisaaniyat_4_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_5_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_6_pts']
# Y0368_voiced_pts_list = ['Sub0271_Lp_Vocal_Y0368_lisaaniyat_4_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_5_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_6_pts']
# Y0365_voiceless_pts_list = ['Sub0256_Lp_Vocal_Y0365_lisaaniyat_7_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_8_pts', 'Sub0256_Lp_Vocal_Y0365_lisaaniyat_9_pts']
# Y0373_voiceless_pts_list = ['Sub0269_Lp_Vocal_Y0373_lisaaniyat_8_pts', 'Sub0269_Lp_Vocal_Y0373_lisaaniyat_9_pts']
# Y0368_voiceless_pts_list = ['Sub0271_Lp_Vocal_Y0368_lisaaniyat_7_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_8_pts', 'Sub0271_Lp_Vocal_Y0368_lisaaniyat_9_pts']                  

# base = plt.gca().transData
# rot = transforms.Affine2D().rotate_deg(90)

# fig, ax = plt.subplots(1,3)
# fig.suptitle('Vocal Tract Contours for /ʕ/ and /ħ/ in Modern Standard Arabic', fontsize = 20)

# for pts in Y0365_voiced_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[0].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
#   ax[0].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

# for pts in Y0365_voiceless_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[0].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
#   ax[0].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

# for pts in Y0373_voiced_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[1].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
#   ax[1].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

# for pts in Y0373_voiceless_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[1].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
#   ax[1].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

# for pts in Y0368_voiced_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/456/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[2].plot('rt_1', 'rt_2', data=pts, color = '#984ea3')
#   ax[2].plot('lf_1', 'lf_2', data=pts, color = '#984ea3')

# for pts in Y0368_voiceless_pts_list:
#   pts_fname = os.path.join('/Volumes/circe/lisaaniyat/data_backup/vt_points/456789/789/%s.csv'%pts)
#   pts = pd.read_csv(pts_fname)
#   # pts['rt_1'] = -pts['rt_1']
#   # pts['lf_1'] = -pts['lf_1']
#   ax[2].plot('rt_1', 'rt_2', data=pts, color = '#ff7f00')
#   ax[2].plot('lf_1', 'lf_2', data=pts, color = '#ff7f00')

# # plt.gca().invert_yaxis()
# ax[0].set_title('Tunisian Speaker', fontsize = 20)
# ax[1].set_title('Egyptian Speaker', fontsize = 20)
# ax[2].set_title('Palestinian Speaker', fontsize = 20)

# labels = ['/ʕ/', '/ħ/']

# from matplotlib.lines import Line2D
# custom_lines = [Line2D([0], [0], color='#984ea3', lw=4),
#                 Line2D([0], [0], color='#ff7f00', lw=4)]
# # ax[0].get_legend().remove()
# # ax[1].get_legend().remove()    
# ax[0].legend(custom_lines, labels)
# ax[1].legend(custom_lines, labels)
# ax[2].legend(custom_lines, labels)
# ax[0].set_xlabel('Distance (mm)', fontsize = 20)
# ax[1].set_xlabel('Distance (mm)', fontsize = 20)
# ax[2].set_xlabel('Distance (mm)', fontsize = 20)
# ax[0].set_ylabel('Distance (mm)', fontsize = 20)
# ax[1].set_ylabel('Distance (mm)', fontsize = 20)
# ax[2].set_ylabel('Distance (mm)', fontsize = 20)

# plt.show()
