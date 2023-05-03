FROM python:3.7

RUN pip install --upgrade pip

RUN pip install pandas==0.24.2 numpy==1.18.5 seaborn==0.9.0 scikit-learn==0.23.2

EXPOSE 7059

COPY test_file.py test_file.py

ENTRYPOINT ["python", "/test_file.py"]
