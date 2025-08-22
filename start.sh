# Install heavy packages at runtime
echo "[INFO] Installing heavy ML packages..."
pip install torch transformers sentence-transformers --no-cache-dir

# Start backend
uvicorn backend.api:app --host 0.0.0.0 --port $BACKEND_PORT &
backend_pid=$!

# Wait a few seconds for backend to start
sleep 5

# Start Streamlit frontend
streamlit run frontend/app.py --server.port $FRONTEND_PORT --server.headless true

# Wait for backend
wait $backend_pid

