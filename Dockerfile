FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pytest --cov=app --cov-report=term-missing || true

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
