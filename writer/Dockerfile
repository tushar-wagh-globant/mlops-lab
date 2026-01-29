FROM python:3.9-slim
WORKDIR /app
COPY app.py .
# Create the shared directory just in case
RUN mkdir -p /app/shared /app/config
CMD ["python", "-u", "app.py"]