FROM python:3.8-slim-buster

WORKDIR /CRUDoperation

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . . 

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]





