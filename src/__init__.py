from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.books.db.main import initdb
from contextlib import asynccontextmanager

version = "v1"


# the lifespan event
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting...")
    await initdb()
    yield
    print("server is stopping")


app = FastAPI(
    title="Book App",
    description="A simple API for managing books",
    version=version,
    lifespan=lifespan,
    # openapi_url=f'/api/v{version}/openapi.json',
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
