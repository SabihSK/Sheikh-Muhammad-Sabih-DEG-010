FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./ /home/app/

ENV PYTHONPATH=${PYTHONPATH}:/home/app/

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

CMD ["bash", "-c", "gunicorn main:app -b 0.0.0.0:5050"]
