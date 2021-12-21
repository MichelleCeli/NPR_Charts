FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./main.py /app
COPY ./requirements.txt /app