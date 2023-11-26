FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/
RUN pip3 install -r requirements.txt && echo "finished"
RUN python3 manage.py collectstatic
