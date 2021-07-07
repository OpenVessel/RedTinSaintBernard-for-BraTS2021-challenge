# RedTinSaintBernard-for-BraTS2021-challenge
Taking-on-BraTS2021-challenge


install req for deeplab testing
https://github.com/google-research/deeplab2/blob/main/g3doc/setup/installation.md
sudo apt-get install protobuf-compiler windows?
git clone https://github.com/tensorflow/models.git

The COCOAPI issue
cocoAPI not on windows so save yourself time use it in ubuntu docker container
https://medium.com/@abinovarghese/installing-coco-api-in-windows-python-9b4dfc3812ef
git clone https://github.com/cocodataset/cocoapi.git
-- cocoapi related issues 
https://github.com/cocodataset/cocoapi/issues/9


remmove lines from setup.py ``` extra_compile_args=[‘-Wno-cpp’, ‘-Wno-unused-function’, ‘-std=c99’] ```
then run ```python setup.py build_ext install```

or use this fork
https://github.com/philferriere/cocoapi

Deeplab requires you convert your dataset to TFRecords its form of binary storage made for TF
read about it here https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564
form of googles protocol buffer

https://stackoverflow.com/questions/13616033/install-protocol-buffers-on-windows

'export' command is valid only for unix shells. In Windows - use 'set' instead of 'export'


<!-- python deeplab2/model/deeplab_test.py -->