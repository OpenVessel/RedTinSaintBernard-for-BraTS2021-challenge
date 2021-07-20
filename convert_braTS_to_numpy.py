
import os
import pandas as pd
from utils import unzip_all_files_folder_2


# df_name_mapping = pd.read_csv(name_mapping)
# df_survival_info = pd.read_csv(survival_info)


outputDir = r"E:\Datasets\BraTS challenge\Output\Output_training"

root_path_train = r"E:\Datasets\BraTS challenge\RSNA_ASNR_MICCAI_BraTS2021_TrainingData"


list_files = os.listdir(root_path_train )

for name_of_file in list_files:
    print(name_of_file)
    #if name_of_file contains .csv it skips iteration on the loop
    if name_of_file.endswith('.csv'):
        continue
    
    #We make new path tto list to for loop through we list that dir
    readable_path = os.path.join(root_path_train , name_of_file)
    
    unzip_all_files_folder_2(readable_path)

