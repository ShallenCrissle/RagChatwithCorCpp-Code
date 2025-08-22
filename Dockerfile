# Base image
FROM python:3.11-slim

# Install only necessary system packages
RUN apt-get update && \
    apt-get install -y clang libclang-dev git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip & install Python dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8080

# Run start.sh
CMD ["bash", "./start.sh"]
