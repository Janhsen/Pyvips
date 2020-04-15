FROM gitpod/workspace-full

RUN apt-get install -y libvips-dev 

RUN pip install pyvips

WORKDIR /data
