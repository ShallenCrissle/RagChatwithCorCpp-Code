# Use lightweight Python base image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y clang libclang-dev git build-essential && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip & install lightweight dependencies only
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose public port
EXPOSE 8080

# Run start.sh
CMD ["bash", "./start.sh"]
