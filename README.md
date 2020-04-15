# Pyvips

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Janhsen/Pyvips) 


## Make a pyvips / python 

### Rebuild the image

```
docker pull python:3
docker build -t pyvips 
```

### Run the demo

```
docker run --rm -t -v $PWD:/data pyvips \
		./wobble.py test.jpg x.jpg
```

