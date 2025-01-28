#FROM python:3.11.4-alpine3.18
FROM cgr.dev/chainguard/python:latest-dev AS builder

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt --user

FROM cgr.dev/chainguard/python:latest

# Make sure you update Python version in path
COPY --from=builder /home/nonroot/.local/lib/python3.13/site-packages /home/nonroot/.local/lib/python3.13/site-packages

WORKDIR /app/
ADD src /app

ENTRYPOINT [ "python", "/app/scanner.py" ]
