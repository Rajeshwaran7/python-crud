FROM python:3.10-slim

WORKDIR /app

# Install required Python packages directly
RUN pip install --no-cache-dir sqlalchemy pymysql fastapi uvicorn

COPY . .

ENV DB_URL=mysql+pymysql://root:root@db/school

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
