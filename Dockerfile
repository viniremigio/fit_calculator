FROM python:3.7

MAINTAINER tiovini

COPY requirements.txt app/
COPY fitapp/* app/fitapp/
COPY data/* app/data/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "fitapp"]