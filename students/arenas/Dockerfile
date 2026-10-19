FROM python:3.12-alpine

WORKDIR /app

# Install wget for healthcheck requests.
RUN apk add --no-cache wget

# Create non-root user for runtime.
RUN addgroup -S app && adduser -S app -G app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Ensure log directory exists and is writable.
RUN mkdir -p /var/log/app && chown -R app:app /var/log/app

USER app

EXPOSE 8080

HEALTHCHECK --interval=10s --timeout=3s --retries=5 \
  CMD wget -qO- http://localhost:8080/health >/dev/null || exit 1

CMD ["python", "/app/app.py"]
