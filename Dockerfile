FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y gcc libffi-dev ffmpeg aria2 build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["python", "./main.py"]
