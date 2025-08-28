FROM python:3.8
WORKDIR /jjbot
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
