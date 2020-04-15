# install dependencies
#Should match Config.py
echo Initializing...

#Create directories to store persistent data
mkdir -p /workspace/conda
mkdir -p /workspace/data

#Create a new env called pyvips
conda create --prefix /workspace/conda/pyvips python=3.7.7 &&
echo "conda activate /workspace/conda/pyvips" >> ~/.bashrc &&
export PATH=/workspace/conda/pyvips/bin:$PATH &&
source ~/.bashrc
export SHELL=/bin/bash

#Install conda packages for to run pyvips
conda install -c conda-forge pyvips

echo Done...
