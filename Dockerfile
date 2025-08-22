# Use prebuilt PyTorch runtime (CPU-only, slim)
FROM pytorch/pytorch:2.8.0-cpu-py3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y clang libclang-dev build-essential git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies (skip torch as it's already included)
RUN pip install --no-cache-dir \
    sentence-transformers \
    transformers \
    chromadb \
    cohere \
    google-generativeai \
    streamlit \
    streamlit-option-menu \
    python-dotenv \
    requests \
    tree-sitter==0.20.4 \
    tree_sitter_languages==1.10.2 \
    uvicorn

# Expose Streamlit port
EXPOSE 8080

# Run start.sh
CMD ["bash", "./start.sh"]
