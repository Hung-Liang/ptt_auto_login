FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /ptt_auto_login

# Install dependencies first so this layer is cached until requirements change
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python3", "main.py"]
