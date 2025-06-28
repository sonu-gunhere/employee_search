from fastapi import FastAPI

from app.apis import search_router



app = FastAPI(title="Employee Search API")


app.include_router(search_router.router, prefix="/search")