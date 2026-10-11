import os
from flask import Flask, jsonify, Response, request

app = Flask(__name__)

STUDENT_NAME = os.getenv("STUDENT_NAME", "Anon")
BARRIO = os.getenv("BARRIO", "Unknown")
LOG_PATH = "/var/log/app/visitas.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


def append_visit_log() -> None:
    # Append each incoming request path to the shared log file.
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(f"{request.method} {request.path}\n")


@app.before_request
def log_request() -> None:
    append_visit_log()


@app.get("/")
def home() -> Response:
    # Build the required greeting using environment variables.
    message = f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}"
    return Response(message, mimetype="text/plain")


@app.get("/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
