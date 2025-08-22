#!/bin/bash
# Ensure LF line endings
set -e

# Ports
FRONTEND_PORT=${PORT:-8501}   # Railway public port
BACKEND_PORT=9000             # Internal backend port

# Start FastAPI backend in background
echo "[INFO] Starting FastAPI backend on port $BACKEND_PORT..."
uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT --log-level info &
backend_pid=$!

# Give backend a few seconds to start
sleep 5

# Start Streamlit frontend
echo "[INFO] Starting Streamlit frontend on port $FRONTEND_PORT..."
streamlit run frontend/app.py --server.port $FRONTEND_PORT --server.headless true

# Wait for backend process
wait $backend_pid
