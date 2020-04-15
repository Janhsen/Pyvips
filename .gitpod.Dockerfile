FROM gitpod/workspace-full

RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y libvips-dev 

RUN pip install pyvips

WORKDIR /data
