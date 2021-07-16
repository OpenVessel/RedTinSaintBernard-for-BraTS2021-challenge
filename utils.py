### 7/13/2021
## utils 
## unzip functions 

import zipfile, os 
import tarfile
import os, gzip, shutil
## BraTS dataset 
## is GZ so unzip it  Gzip compression
def unzip_all_files_folder_2(directory):
# https://gist.github.com/kstreepy/a9800804c21367d5a8bde692318a18f5
    extension = ".gz"
    os.chdir(directory)
    for item in os.listdir(directory): # loop through items in dir
        if item.endswith(extension): # check for ".gz" extension
            gz_name = os.path.abspath(item) # get full path of files
            file_name = (os.path.basename(gz_name)).rsplit('.',1)[0] #get file name for file within
            with gzip.open(gz_name,"rb") as f_in, open(file_name,"wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(gz_name) # delete zipped file

## broken function
def unzip_all_files_folder_1(path):
    os.chdir(path)
    print(path)
    list_of_zips = os.listdir(path)

    print(list_of_zips)
    for file in list_of_zips:   
        print(file)# get the list of files
    if tarfile.is_tarfile(file):
        opened_tar.extractall(path)
    else:
        print("The tar file you entered is not a tar file")

        if zipfile.is_zipfile(file): # if it is a zipfile, extract it
            with zipfile.ZipFile(file) as item: # treat the file as a zip
                item.extractall()  # extract it in the working directory


import numpy as np
import nibabel as nib
img = nib.load(example_filename)
a = np.array(img.dataobj)

## function to convert .nii files to numpy arrays
def nii_to_numpy():
    for f in filenames:
    #Start reading nii files
        f_folder = f[:-8]
        img_path = os.path.join(input_path, f)
        if os.path.isfile(img_path):
            img = nib.load(img_path) #read nii
            img_fdata = img.get_fdata()