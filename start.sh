#!/bin/bash
set -e

FRONTEND_PORT=${PORT:-8501}   # Streamlit frontend port
BACKEND_PORT=9000             # Internal backend port

# Install heavy packages at runtime to reduce image size
echo "[INFO] Installing heavy Python packages..."
pip install --no-cache-dir torch transformers sentence-transformers chromadb

echo "[INFO] Starting FastAPI backend on port $BACKEND_PORT..."
uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT &
backend_pid=$!

sleep 5  # Give backend time to start

echo "[INFO] Starting Streamlit frontend on port $FRONTEND_PORT..."
streamlit run frontend/app.py --server.port $FRONTEND_PORT --server.headless true

wait $backend_pid
