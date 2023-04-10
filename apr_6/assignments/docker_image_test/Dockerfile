#FROM ubuntu

#RUN apt-get update
#RUN apt-get install -y python3
#RUN apt-get install -y pip
#RUN pip install pandas

#COPY test.py test.py

#ENTRYPOINT ['python3', '/test.py']

FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install pandas

COPY test.py test.py

ENTRYPOINT ["python3", "/test.py"]
