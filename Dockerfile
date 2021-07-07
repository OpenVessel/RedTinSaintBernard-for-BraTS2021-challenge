## Start from this Docker image
FROM ubuntu

## Install R in Docker image
RUN apt-get update 
RUN apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file/50339110
# jsut call pip install requirements pathing issues TO-DO

RUN apt-get install python3
RUN pip3 install --no-cache-dir -e git+https://github.com/neuronflow/BraTS-Toolkit-Source.git@62b33277390e64737880f8e826a598d0571fa098#egg=brats_toolkit
RUN pip3 install --no-cache-dir certifi==2021.5.30
RUN pip3 install --no-cache-dir chardet==3.0.4
RUN pip3 install --no-cache-dir idna==2.10
RUN pip3 install --no-cache-dir joblib==1.0.1
RUN pip3 install --no-cache-dir numpy==1.20.1
RUN pip3 install --no-cache-dir pandas==1.3.0
RUN pip3 install --no-cache-dir python-dateutil==2.8.1
RUN pip3 install --no-cache-dir python-engineio==3.14.2
RUN pip3 install --no-cache-dir python-socketio==4.6.1
RUN pip3 install --no-cache-dir pytz==2021.1
RUN pip3 install --no-cache-dir requests==2.24.0
RUN pip3 install --no-cache-dir scikit-learn==0.24.2
RUN pip3 install --no-cache-dir scipy==1.7.0
RUN pip3 install --no-cache-dir SimpleITK==2.0.2
RUN pip3 install --no-cache-dir six==1.16.0
RUN pip3 install --no-cache-dir sklearn==0.0
RUN pip3 install --no-cache-dir threadpoolctl==2.1.0
RUN pip3 install --no-cache-dir urllib3==1.25.11


## Copy your files into Docker image
#  How to copy files into Docker image? 
COPY model.py /usr/local/bin/
# COPY model.rds /usr/local/bin/
RUN chmod a+x /usr/local/bin/model.py

## Make Docker container executable
ENTRYPOINT ["pythonscript", "/usr/local/bin/model.py"]