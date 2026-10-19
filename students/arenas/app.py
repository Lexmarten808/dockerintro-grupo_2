import os
from flask import Flask, jsonify, Response

app = Flask(__name__)

# Read values from environment with required defaults.
STUDENT_NAME = os.getenv("STUDENT_NAME", "Anon")
BARRIO = os.getenv("BARRIO", "Unknown")
LOG_PATH = "/var/log/app/visitas.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


@app.get("/")
def home() -> Response:
    message = f"Hola, I am {STUDENT_NAME} and I live in {BARRIO}"

    # Append one line per request to the shared log file.
    with open(LOG_PATH, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

    return Response(message, mimetype="text/plain")


@app.get("/health")
def health():
    return jsonify({"ok": True}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
