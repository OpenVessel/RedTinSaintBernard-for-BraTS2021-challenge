
pathway = "E:\Datasets\BraTS challenge\BraTS2020_training_data\content\data"

# .h5 dataformat?
# volume slices?

## Install HD-BET? https://github.com/MIC-DKFZ/HD-BET
## Install ROBEX RObust Brain Extraction https://www.nitrc.org/projects/robex


### GUI https://neuronflow.github.io/BraTS-Preprocessor/index.html 

## convert .h5? Hierarchical Data Format version 5 (HDF5)
#https://stackoverflow.com/questions/28170623/how-to-read-hdf5-files-in-python

import os
from path import Path
from brats_toolkit.preprocessor import Preprocessor

# Code from BraTS toolKit
# instantiate
prep = Preprocessor()
inputDir = "example_data/input_preprocessor_batch_processing/exams_to_preprocess"
outputDir = "example_data/output_preprocessor_batch"
# execute it
prep.batch_preprocess(exam_import_folder=inputDir,
                      exam_export_folder=outputDir, mode="gpu", confirm=True, skipUpdate=False, gpuid='0')