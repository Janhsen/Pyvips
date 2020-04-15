FROM gitpod/workspace-full

RUN sudo apt-get install -y libvips-dev 

RUN pip3 install pyvips

WORKDIR /data
