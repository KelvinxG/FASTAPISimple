FROM python:3.11.1

WORKDIR /FASTRESTSIMPLE

RUN apt-get update &&\
    apt-get install -y --no-install-recommends gcc

COPY ./requirements.txt /FASTRESTSIMPLE/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
