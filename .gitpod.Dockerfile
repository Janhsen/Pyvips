FROM gitpod/workspace-full

RUN sudo apt-get update
RUN sudo apt-get install -y libvips-dev 

RUN pip3 install pyvips opcua


#inlets
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    # 'cosmic' not supported
    && add-apt-repository -yu "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" \
    && apt-get install -yq docker-ce-cli=5:18.09.0~3-0~ubuntu-bionic \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

USER gitpod
RUN brew install inlets


WORKDIR /data
