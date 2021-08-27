FROM python:3.7

WORKDIR /app
ADD ./model ./model
ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
