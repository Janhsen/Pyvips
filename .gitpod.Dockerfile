FROM gitpod/workspace-full
USER root

RUN apt-get update
RUN apt-get install -y libvips-dev 
RUN pip3 install pyvips

WORKDIR /data
