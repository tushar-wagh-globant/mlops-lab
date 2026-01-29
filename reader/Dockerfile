FROM python:3.9-slim
WORKDIR /app
# Install Postgres library
RUN pip install psycopg2-binary
COPY app.py .
CMD ["python", "-u", "app.py"]