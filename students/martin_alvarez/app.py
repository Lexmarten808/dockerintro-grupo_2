import os
from datetime import datetime
from pathlib import Path

from flask import Flask, Response, jsonify

app = Flask(__name__)

# Read service identity from environment.
STUDENT_NAME = os.getenv("STUDENT_NAME", "Anon")
BARRIO = os.getenv("BARRIO", "Unknown")
LOG_FILE = "/var/log/app/visitas.log"
Path("/var/log/app").mkdir(parents=True, exist_ok=True)


def append_visit(message: str) -> None:
    """Append each visit to the shared visits log."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            timestamp = datetime.now().isoformat(timespec="seconds")
            file.write(f"{timestamp} {message}\n")
    except OSError:
        # Keep service available even if log volume is unavailable.
        pass


@app.get("/")
def home() -> Response:
    message = f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}"
    append_visit(message)
    return Response(message, mimetype="text/plain")


@app.get("/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
