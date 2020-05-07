FROM gitpod/workspace-full
USER root

RUN apt-get update
RUN apt-get install -y libvips-dev 
RUN pip3 install pyvips opcua

#inlets
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add 

Run curl -LkO https://raw.githubusercontent.com/remoteit/installer/master/scripts/auto-install.sh
Run chmod +x ./auto-install.sh
Run ./auto-install.sh

USER gitpod
RUN brew install inlets

WORKDIR /data
