FROM python:3

RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y libvips-dev 

RUN pip3 install pyvips

COPY ImageProcessing.py /data
COPY OPCUAServer.py /data

CMD [ "python", "/data/OPCUAServer.py" ]

WORKDIR /data
