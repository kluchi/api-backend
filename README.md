# Taxinder api

This repository contains main api code of our application

## Building

You can use docker to build and run the application:

```bash
docker build -t cluchi-api . && \
docker run -it -p 8080:8080 cluchi-api
```

Alternatively, you can manually install dependencies with `pip install -r requirements.txt` and run main script with `python src/main.py`.

## Configuration

Configuration is performed via environment variables

| parameter | default | description |
| --- | --- | --- |
| `SERVER_PORT` | `8080` | port the application runs on. Do not forget to also change it in docker run command |
| `SERVER_BIND_IP` | `0.0.0.0` | interface for uvicorn to bind to |
| `API_BASE_PATH` | `/` | base path of the application. You may want to change it if running behind reverse proxy (eg nginx) |
