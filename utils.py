### 7/13/2021
## utils 
## unzip functions 
## for looping converting nii files into PNG to visualize


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


# import numpy as np
# import nibabel as nib

# img = nib.load(example_filename)
# a = np.array(img.dataobj)

# ## function to convert .nii files to numpy arrays
# def nii_to_numpy():
#     for f in filenames:
#     #Start reading nii files
#         f_folder = f[:-8]
#         img_path = os.path.join(input_path, f)
#         if os.path.isfile(img_path):
#             img = nib.load(img_path) #read nii
#             img_fdata = img.get_fdata()


import os 
import nibabel
import imageio 

# cwd = os.getcwd()
# E:\Datasets\BraTS challenge\RSNA_ASNR_MICCAI_BraTS2021_TrainingData
#os.list
def convert_nii_to_png(root_path):
        
    file_path = root_path

    new_dirs = [os.path.join(file_path, 'brain_flair'),
                    os.path.join(file_path, 'brain_t1'),
                    os.path.join(file_path, 'brain_t1ce'),
                    os.path.join(file_path, 'seg'),
                    os.path.join(file_path, 'brain_t2')]

    for dir in new_dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)

    for file in os.listdir(file_path):
        
        
        file_name = os.path.join(file_path, file)
        
        if os.path.isfile(file_name) and file == "00000534_brain_t2.nii":
            file_array = nibabel.load(file_array).get_fdata() #Loads our data with nibabel

        print("Loading ", file)
        for i in range(file_array.shape[2]):
            if 'brain_flair' in str(os.listdir(file_path)):
                print('Saving to flair folder')
                s = file_array[:,:,i]
                imageio.imwrite(os.path.join(new_dirs[0], 'slice_{}.png'.format(i)), s)

            if 'brain_t1' in str(os.listdir(file_path)):
                print('Saving to t1 folder')
                s = file_array[:,:,i]
                imageio.imwrite(os.path.join(new_dirs[1], 'slice_{}.png'.format(i)), s)

            if 'brain_t1ce' in str(os.listdir(file_path)):
                print('Saving to t1ce folder')
                s = file_array[:,:,i]
                imageio.imwrite(os.path.join(new_dirs[2], 'slice_{}.png'.format(i)), s)

            if 'seg' in str(os.listdir(file_path)):
                print('Saving to seg folder')
                s = file_array[:,:,i]
                imageio.imwrite(os.path.join(new_dirs[3], 'slice_{}.png'.format(i)), s) 

            if 'brain_t2' in str(os.listdir(file_path)):
                print('Saving to t2 folder')
                s = file_array[:,:,i]
                imageio.imwrite(os.path.join(new_dirs[4], 'slice_{}.png'.format(i)), s) 