FROM gitpod/workspace-full

RUN sudo apt-get install -y libvips-dev 

RUN pip install pyvips

WORKDIR /data
