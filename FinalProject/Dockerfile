FROM python:3.10.0

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt  /app/requirements.txt
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "__main__.py"]




