FROM python:3
Maintainer xorob00

RUN pip3 install libtorrent 

COPY ./yolo-restore.py ./

CMD ["python", "./yolo-restore.py"] 
