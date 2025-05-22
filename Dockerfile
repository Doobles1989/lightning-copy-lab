FROM python:3.10
WORKDIR /app
COPY ./api ./api
COPY ./services ./services
COPY ./utils ./utils
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
