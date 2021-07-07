import os
import pandas as pd
from brats_toolkit.preprocessor import Preprocessor
# instantiate
prep = Preprocessor()

## convert mapping info
## survial 
name_mapping = r"E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\name_mapping.csv"
survival_info = r"E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\survival_info.csv"

df_name_mapping = pd.read_csv(name_mapping)
df_survival_info = pd.read_csv(survival_info)

root_path_train = r"E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData"
outputDir = r"E:\Datasets\BraTS challenge\Output\Output_training"
list_of_dir = os.listdir(root_path_train)

for name_of_file in list_of_dir:
    
    #if name_of_file contains .csv it skips iteration on the loop
    if name_of_file.endswith('.csv'):
        continue
    
    #We make new path tto list to for loop through we list that dir
    readable_path = os.path.join(root_path_train , name_of_file)
    list_of_zips = os.listdir(readable_path)
    
    # we for loop each folder
    list_sort = []
    outpath = os.path.join(outputDir, name_of_file)

    for zips in list_of_zips:
        
        readable_path_2nd = os.path.join(readable_path, zips)
        list_sort.append(readable_path_2nd)
        list_sort = sorted(list_sort)
        ## missing var for segmentation preprocessing # E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\BraTS20_Training_369\BraTS20_Training_369_seg.nii.gz 2 ??

    examName = name_of_file
    flaFile = list_sort[0] #  E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\BraTS20_Training_369\BraTS20_Training_369_flair.nii.gz1 flaFile
    t1File = list_sort[2] # E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\BraTS20_Training_369\BraTS20_Training_369_t1.nii.gz 3 t1File
    t1cFile = list_sort[3] # E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\BraTS20_Training_369\BraTS20_Training_369_t1ce.nii.gz 4 t1cFile
    t2File = list_sort[4] # E:\Datasets\BraTS challenge\MICCAI_BraTS2020_TrainingData\BraTS20_Training_369\BraTS20_Training_369_t2.nii.gz 5 t2File

    ## this code calls docker!
    ##dcm2niix conversion 
    prep.single_preprocess(t1File=t1File, 
        t1cFile=t1cFile, 
        t2File=t2File, 
        flaFile=flaFile,
        outputFolder=outputDir, 
        mode="cpu", 
        confirm=True, 
        skipUpdate=False, 
        gpuid='0')


            # start_docker(exam_import_folder=exam_import_folder, exam_export_folder=exam_export_folder,
            #              dicom_import_folder=dicom_import_folder, nifti_export_folder=nifti_export_folder, mode=self.mode, gpuid=self.gpuid)


## expected outtputs?
#hdbet_brats-space
#hdbet_native-space
#mask_hdbet_brats-space
#masks_hdbet-space
#niftis_brats-space
#png_slices
#registrations
