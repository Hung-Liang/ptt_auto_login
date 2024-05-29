FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Hung-Liang/ptt_auto_login

COPY .env ptt_auto_login/.env

RUN cd ptt_auto_login && pip install -r requirements.txt

CMD ["cd", "ptt_auto_login", "&&", "python", "main.py"]
