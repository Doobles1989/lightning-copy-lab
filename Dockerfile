FROM python:3.10

WORKDIR /app

COPY ./api ./api
COPY ./services ./services
COPY ./utils ./utils
COPY requirements.txt .
COPY .env.example .env  # Optional
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Expose the port the app runs on