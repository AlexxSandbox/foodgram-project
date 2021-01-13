FROM python:3.8.5
LABEL description="Foodgram project" author="A.Sergeev"
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt