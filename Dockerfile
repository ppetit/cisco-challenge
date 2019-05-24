FROM python:3
ADD movie-rating.py /
RUN pip install omdb>=0.10.1 
ENTRYPOINT [ "python", "./movie-rating.py" ]
CMD [ "-h" ]
