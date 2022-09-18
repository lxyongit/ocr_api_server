FROM python:3.8-slim-buster

RUN mkdir /app

COPY ./*.txt ./*.py ./*.sh ./*.onnx /app/


RUN cd /app \
    && python3 -m pip install --upgrade pip \
    && pip3 install -r requirements.txt \
    # && rm -rf /tmp/* && rm -rf /root/.cache/* \
    # && sed -i 's#http://deb.debian.org#http://mirrors.aliyun.com/#g' /etc/apt/sources.list\
    && apt-get --allow-releaseinfo-change update && apt install libgl1-mesa-glx libglib2.0-0 -y

WORKDIR /app

CMD ["python3", "ocr_server.py", "--port", "9898", "--ocr", "--det"]
