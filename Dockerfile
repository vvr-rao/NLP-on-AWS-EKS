FROM python:3.7

WORKDIR /app
ADD ./model ./model
ADD main.py main.py
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
