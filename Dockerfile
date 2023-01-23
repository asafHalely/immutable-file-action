FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y git

COPY requirement.txt .
RUN pip3 install -r requirement.txt

ADD . .

ENTRYPOINT ["python3","/app/main.py"]
