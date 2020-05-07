FROM gitpod/workspace-full
USER root

RUN apt-get update
RUN apt-get install -y libvips-dev 
RUN pip3 install pyvips opcua

#inlets
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add 
RUN curl https://i.jpillora.com/chisel! | bash

USER gitpod
RUN brew install inlets

WORKDIR /data
