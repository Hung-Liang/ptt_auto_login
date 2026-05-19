FROM python:3.11-slim-bullseye

# Install git and clean up apt cache to reduce image size
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /ptt_auto_login

# Clone the repository into the current WORKDIR
RUN git clone https://github.com/Hung-Liang/ptt_auto_login .

# Copy environment variables
COPY .env .env

# Install dependencies with the upgraded Python environment
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]