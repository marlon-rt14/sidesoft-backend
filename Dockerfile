FROM python:3.11.1
WORKDIR /code
COPY . .

ENV DEBUG=False
ENV SERVER_PORT=5000
ENV SECRET_KEY=whoismarlon

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "./server/index.py"]