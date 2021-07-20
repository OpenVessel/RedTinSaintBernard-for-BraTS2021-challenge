path_to_single = r"E:\Datasets\BraTS challenge\BraTS2021_00621"

path_to_BraTS2021 = "E:\Datasets\BraTS challenge\RSNA_ASNR_MICCAI_BraTS2021_TrainingData"

## What is flair 
## What is seg 
## What is t1 
## What is t1ce 
## What is t2?

## So we need to unzip the data points 
from utils import unzip_all_files_folder_2, convert_nii_to_png
## function works for a single folder we can for loop all folders
# unzip_all_files_folder_2(path_to_single)
convert_nii_to_png(path_to_single)
## read in the nitfi files into numpy arrays 

import numpy as np
import nibabel as nib
import itk
# Packages 
# itkwidgets
# nibabel 
# img = nib.load(example_filename)
# a = np.array(img.dataobj)



## visualize the data somehow

## Training set and the test set



## Apply Agglomerative Hierarchical clustering
## Apply Divisive Hierarchical clustering technique 

## What I found interesting Calculate the similarity between two clusters?
# MIN, MAX, Group Average, Distance between Centroids, Ward's Method's ## How can any of these be similar to 
# Dice SImilarity Coefficient or Hausdorff distance 
# https://towardsdatascience.com/understanding-the-concept-of-hierarchical-clustering-technique-c6e8243758ec