FROM gitpod/workspace-full
USER root

RUN apt-get update
RUN apt-get install -y libvips-dev python3-lxml python-lxml libxml2-dev libxslt-dev python-dev
RUN pip3 install pyvips opcua scipy matplotlib ipython jupyter pandas sympy nose pint
RUN curl https://i.jpillora.com/chisel! | bash

USER gitpod	
RUN brew install inlets	

WORKDIR /data
