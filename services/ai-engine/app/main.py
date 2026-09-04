from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AI Code Evaluation Engine",
    version="0.1.0",
)

app.include_router(router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}