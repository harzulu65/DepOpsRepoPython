FROM python:3.8-slim-buster

WORKDIR /CRUDoperation

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . . 

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





