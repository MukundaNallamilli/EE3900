FROM ubuntu:latest

RUN  apt-get update
RUN apt-get install python3 -y
RUN apt-get install libffi-dev libsndfile1 -y
RUN apt install python3-pip -y
RUN  pip3 install numpy scipy matplotlib
RUN  pip3 install cffi pysoundfile
WORKDIR /app
COPY ./2-2.py  2-2.py
COPY ./Sound_Noise.wav  Sound_Noise.wav
CMD ["python3","2-2.py"]
