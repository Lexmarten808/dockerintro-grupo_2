import os
from pathlib import Path

from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# Read identity values from environment variables.
STUDENT_NAME = os.getenv("STUDENT_NAME", "Anon")
BARRIO = os.getenv("BARRIO", "Unknown")
LOG_FILE = "/var/log/app/visitas.log"
Path("/var/log/app").mkdir(parents=True, exist_ok=True)


@app.before_request
def append_visit() -> None:
    """Append each request to the shared visits log."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{request.method} {request.path}\n")
    except OSError:
        # Keep serving requests if the log volume is unavailable.
        pass


@app.get("/")
def home() -> Response:
    message = f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}"
    return Response(message, mimetype="text/plain")


@app.get("/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
