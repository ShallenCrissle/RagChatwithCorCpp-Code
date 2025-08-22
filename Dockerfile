# Base image
FROM python:3.11-slim

# Install only necessary system packages
RUN apt-get update && \
    apt-get install -y clang libclang-dev git curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip & install lightweight dependencies
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements_light.txt

# Expose Streamlit port
EXPOSE 8080

# Make start.sh executable
RUN chmod +x start.sh

# Run start.sh
CMD ["bash", "./start.sh"]
