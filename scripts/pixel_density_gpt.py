#### pixel density

import cv2
import numpy as np

def select_roi(frame):
    """ Function to select ROI on the first frame """
    # Resize the frame to make the ROI selection window bigger
    resized_frame = cv2.resize(frame, (frame.shape[1]*3, frame.shape[0]*3))
    r = cv2.selectROI("Select Region", resized_frame)
    
    # Adjust ROI coordinates to match the original frame size
    r = tuple([int(coord / 3) for coord in r])
    return r

def process_frame(frame, roi):
    """ Function to process each frame """
    x, y, w, h = roi
    roi_frame = frame[y:y+h, x:x+w]
    # Compute pixel density or any other metric here
    pixel_density = np.mean(roi_frame)
    return pixel_density

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    success, first_frame = cap.read()

    if not success:
        print("Failed to read the video")
        return

    roi = select_roi(first_frame)
    
    # Close all OpenCV windows
    cv2.destroyAllWindows()

    pixel_densities = []

    while True:
        success, frame = cap.read()
        if not success:
            break

        pixel_density = process_frame(frame, roi)
        pixel_densities.append(pixel_density)

    cap.release()
    return pixel_densities

# Replace 'path_to_video.avi' with your actual video file path
pixel_densities = main('/Volumes/circe/lisaaniyat/data_backup/avi/Sub0149_Lp_Vocal_Y0376_lisaaniyat_1.avi')
print(pixel_densities)

### all subjects ###

import cv2
import numpy as np
import glob
import os
import re
import pandas as pd
from skimage.filters import threshold_otsu

def select_roi(frame):
    """ Function to select ROI on the frame """
    resized_frame = cv2.resize(frame, (frame.shape[1]*3, frame.shape[0]*3))
    r = cv2.selectROI("Select ROI", resized_frame)
    r = tuple([int(coord / 3) for coord in r])
    cv2.destroyAllWindows()
    return r

def segment_roi(frame, roi):
    """ Apply basic segmentation within the ROI """
    x, y, w, h = roi
    roi_frame = frame[y:y+h, x:x+w]
    gray_roi = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)
    thresh = threshold_otsu(gray_roi)
    binary_roi = gray_roi > thresh
    return binary_roi

def process_frame(frame, roi):
    """ Function to process each frame """
    binary_roi = segment_roi(frame, roi)
    pixel_density = np.mean(binary_roi)

    # Highlight the ROI
    highlighted_frame = frame.copy()
    cv2.rectangle(highlighted_frame, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), (0, 255, 0), 2)
    return pixel_density, highlighted_frame

def analyze_videos(subject_videos, roi=None):
    results = []

    for video_path in subject_videos:
        cap = cv2.VideoCapture(video_path)
        success, frame = None, None
        for _ in range(4):  # Skip to 4th frame
            success, frame = cap.read()

        if not success:
            print(f"Failed to read the video {video_path}")
            continue

        if roi is None:
            roi = select_roi(frame)

        frame_number = 0
        avi_filename = os.path.basename(video_path)
        run_number = re.search(r"(\d+)\.avi$", avi_filename)

        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to first frame

        while True:
            success, frame = cap.read()
            if not success:
                break

            pixel_density, highlighted_frame = process_frame(frame, roi)
            results.append({
                "Subject": subject_number,
                "ROI": roi,
                "Frame": frame_number,
                "Density": pixel_density,
                "avi": avi_filename,
                "Run": int(run_number.group(1)) if run_number else None
            })

            # Save the highlighted frame as PNG
            output_dir = "output_frames"
            os.makedirs(output_dir, exist_ok=True)
            output_filename = f"{output_dir}/{subject_number}_Run{run_number.group(1)}_Frame{frame_number}.png"
            cv2.imwrite(output_filename, highlighted_frame)

            frame_number += 1

        cap.release()

    return results

# Path to the directory containing the .avi files
avi_files_directory = "/Volumes/circe/lisaaniyat/data_backup/avi/"

# Get all .avi files
avi_files = glob.glob(os.path.join(avi_files_directory, "*.avi"))

# Group files by subject
subject_files = {}
for file in avi_files:
    subject_number = re.search(r"Y\d{4}", file)
    if subject_number:
        subject_number = subject_number.group()
        subject_files.setdefault(subject_number, []).append(file)

all_data = []

for subject_number, videos in subject_files.items():
    subject_results = analyze_videos(videos)
    all_data.extend(subject_results)

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(all_data, columns=['Subject', 'ROI', 'Frame', 'Density', 'avi', 'Run'])

# Display or save the DataFrame
print(df)

# Optionally, save to CSV
df.to_csv('/Volumes/circe/lisaaniyat/analysis/pixel_density_data.csv', index=False)



