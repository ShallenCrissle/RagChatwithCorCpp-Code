#!/bin/bash
# start.sh - Run FastAPI backend and Streamlit frontend
# Make sure this file has LF line endings

set -e

# Default ports
FRONTEND_PORT=${PORT:-8501}   # Streamlit frontend
BACKEND_PORT=9000             # Internal backend

# Install heavy ML packages at runtime
echo "[INFO] Installing heavy ML packages..."
pip install --no-cache-dir torch transformers sentence-transformers chromadb

# Start FastAPI backend
echo "[INFO] Starting FastAPI backend on port $BACKEND_PORT..."
uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT &
backend_pid=$!

# Give backend time to start
sleep 5

# Start Streamlit frontend
echo "[INFO] Starting Streamlit frontend on port $FRONTEND_PORT..."
streamlit run frontend/app.py --server.port $FRONTEND_PORT --server.headless true

# Wait for backend to finish
wait $backend_pid
