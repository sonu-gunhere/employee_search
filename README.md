# Employee Search API

## Features
- Search employees with filters
- Organization-specific visible columns
- In-memory IP rate limiting (custom, no external lib)
- Unit tested with `pytest`
- Dockerized
- OpenAPI/Swagger auto-generated


## Project Structure
```
app/
├── main.py              # FastAPI entrypoint
├── apis/                # API routes
├── services/            # Business logic
├── models/              # we can define the db models
├── schemas/             # enums and data validation
├── utils/               # Config (rate limits etc.)
├── tests/               # Unit tests
└── ...

```
---
##  Run Tests
```bash
pytest --cov=app --cov-report=term-missing
```
---
## Run via Docker
### Build
```bash
docker build -t employee-search .
```
### Run
```bash
docker run -p 8000:8000 employee-search
```

---

## API Docs
After starting:
- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc
- OpenAPI JSON: http://localhost:8000/openapi.json

---

## Tech Stack
- FastAPI
- Uvicorn
- Pytest + Coverage
- Python 3.12
- Docker (Slim image)

---

## How to Use
Call the endpoint:
```
GET /search/?org_id=org1&query=John&status=Active&page=1&size=10
```

---

## Sample Data
- 3 Organizations: `org1`, `org2`, `org3`
- 4 Companies: TCS, Infosys, HCL, Wipro
- 6 Employees with diverse fields

---

## Notes
- No database — uses in-memory Python data for simplicity
- No external libraries used for rate limiting (as required)
- No auth or login included (out of scope)

---