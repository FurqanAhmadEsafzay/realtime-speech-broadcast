FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY app ./app
COPY client ./client
COPY recordings ./recordings
COPY model ./model

# Expose WebSocket port
EXPOSE 8765

# Run application as module
CMD ["python", "-m", "app.main"]
