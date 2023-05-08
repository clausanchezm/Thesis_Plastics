FROM tensorflow/tensorflow:latest-gpu-jupyter
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

