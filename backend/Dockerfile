# Use CPU-only slim PyTorch image
FROM pytorch/pytorch:2.8.0-cpu-py3.11-slim

# System dependencies
RUN apt-get update && \
    apt-get install -y clang libclang-dev build-essential git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy backend code
COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install only necessary Python packages
RUN pip install --no-cache-dir \
    sentence-transformers \
    transformers \
    cohere \
    google-generativeai \
    chromadb \
    tree-sitter==0.20.4 \
    tree_sitter_languages==1.10.2 \
    uvicorn \
    python-dotenv \
    requests

# Expose FastAPI port
EXPOSE 9000

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "9000"]
