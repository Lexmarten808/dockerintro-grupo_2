---
name: Student service
about: Individual service Issue (to be implemented with GitHub Copilot)
title: "[Service] <Your name> - <Neighborhood>"
labels: student-service
---

## Student
- Name:
- Folder: `/students/<your-name>/`

## Neighborhood (Docker network)
- Name: (e.g. san-antonio, granada, ciudad-jardin)

## Technology stack
- [ ] Python (Flask)
- [ ] Node.js (Express)
- [ ] Nginx (static)
- [ ] Other:

## Service behavior
- Listens on port `8080`
- `GET /` responds with plain text: `Hola, I am <YourName> and I live in <Neighborhood>`
- Every request to `/` is appended to `/var/log/app/visitas.log`

## Environment variables
- `STUDENT_NAME`: student name (default `Anon`)
- `BARRIO`: neighborhood name (default `Unknown`)

## Logging requirement
- Write every request to `/var/log/app/visitas.log`
- The path is mounted from the shared volume `biblioteca-del-pueblo`

## Health endpoint
- `GET /health` returns HTTP 200 with `{"ok": true}`

## Docker image requirement
- Dockerfile inside `/students/<your-name>/`
- Runs as a non-root user
- Includes `EXPOSE 8080` and a `HEALTHCHECK`
- Published to Docker Hub or GitHub Packages (`ghcr.io`) with tag `v1`

## Acceptance criteria
- [ ] `docker build` succeeds
- [ ] Container runs in the assigned network with the `biblioteca-del-pueblo` volume mounted
- [ ] `curl http://localhost:<port>` returns the expected message
- [ ] `/health` returns 200
- [ ] Requests appear in `visitas.log` inside the shared volume
- [ ] Another container in the same network can reach `http://svc-<name>:8080/`
- [ ] Only files inside `/students/<your-name>/` were changed

## Notes for Copilot
Implement only inside `/students/<your-name>/`. Keep the code simple and add short comments.
