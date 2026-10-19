import os
from pathlib import Path
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Read identity from environment.
STUDENT_NAME = os.getenv("STUDENT_NAME", "Anon")
BARRIO = os.getenv("BARRIO", "Unknown")
LOG_FILE = "/var/log/app/visitas.log"
Path("/var/log/app").mkdir(parents=True, exist_ok=True)


def append_visit(greeting: str) -> None:
    """Append root greeting requests to the shared visits log."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{greeting}\n")
    except OSError:
        # Keep serving traffic even if the shared volume is not writable.
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
