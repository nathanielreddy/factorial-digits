FROM python:3.8

WORKDIR /app

COPY factorial-digits.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./factorial-digits.py"]
