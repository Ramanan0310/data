"""Production server entry point for domain deployment."""

import os

from waitress import serve

from app import app, init_db

if __name__ == "__main__":
    init_db()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    print(f"AC073-VANUR running on http://{host}:{port}")
    serve(app, host=host, port=port, threads=4)
