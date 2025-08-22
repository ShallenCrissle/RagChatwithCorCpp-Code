#!/bin/bash
# start.sh - Runs FastAPI backend and Streamlit frontend
# Ensure LF line endings before deploying

# Exit immediately if a command fails
set -e

# Railway exposes a single $PORT for public access
FRONTEND_PORT=${PORT:-8501}   # Streamlit uses this port
BACKEND_PORT=9000             # Internal backend port

echo "[INFO] Starting FastAPI backend on port $BACKEND_PORT..."
uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT &
backend_pid=$!

# Wait a few seconds for backend to start
sleep 5

echo "[INFO] Starting Streamlit frontend on port $FRONTEND_PORT..."
streamlit run frontend/app.py --server.port $FRONTEND_PORT --server.headless true

# Wait for the backend process
wait $backend_pid
