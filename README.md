# Employee Search API

## Features
- FastAPI search API for employee directory
- Organization-specific dynamic columns
- In-memory rate-limiting (no external lib)
- OpenAPI schema auto-generated
- Dockerized and unit-tested

## Run Locally
```bash
git clone <repo>
cd employee_search
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Docker
```bash
docker build -t employee-search .
docker run -p 8000:8000 employee-search
```

## Test
```bash
pytest app/tests/
```
