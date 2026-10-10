# Instructions for GitHub Copilot

This repo is a Docker lab. Each student owns one folder: `/students/<name>/`.

- Only create or modify files inside the folder named in the Issue.
- Services must listen on port 8080 and bind to 0.0.0.0.
- `GET /` returns `Hola, I am <STUDENT_NAME> and I live in <BARRIO>` as plain text.
- Read `STUDENT_NAME` and `BARRIO` from environment variables.
- Append every request to `/var/log/app/visitas.log`.
- Provide `GET /health` returning HTTP 200 and `{"ok": true}`.
- Dockerfile: small base image (alpine), non-root user, `EXPOSE 8080`, `HEALTHCHECK`.
- Keep code simple and commented; no unnecessary dependencies.
