## Image classification to catategorize all pixels in a digital image into one of several land cover classes or themes 
## Neural Network # Perpectron Single layer for linear data #inputs weights bias function transformation function
## layer accepts inputs ## Hidden Layer ## Output Layers

## MNIST dataset its dataset of 60,000  small square 28x28 pixels grayscale images of handwritten single digist between 0-9

## Import Data Set 
## Explore the data 
## Preprocess the data 
## Build the model 
## Set up Layers 
## Set up Layers 
## Compile the model 
## Train the model 
# Evaluation and Predictions 
import os 
import nibabel
import imageio 

cwd = os.getcwd()

file_path = os.path.join(cwd, 'test_files')

new_dirs = [os.path.join(file_path, 'brain_flair'),
                os.path.join(file_path, 'brain_t1'),
                os.path.join(file_path, 'brain_t1ce'),
                os.path.join(file_path, 'seg'),
                os.path.join(file_path, 'brain_t2')]

for dir in new_dirs:
    if not os.path.exists(dir):
        os.mkdir(dir)

for file in os.listdir(file_path):
    
    
    file_array = os.path.join(file_path, file)
    if os.path.isfile(file_array):
        file_array = nibabel.load(file_array).get_fdata()

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