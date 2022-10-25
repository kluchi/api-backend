FROM python:3.11-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src

EXPOSE 8080
ENTRYPOINT [ "python", "src/main.py" ]