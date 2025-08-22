# Base image with Python
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y clang libclang-dev build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8080

# Run start.sh
CMD ["bash", "./start.sh"]
