from fastapi import FastAPI

app = FastAPI(
    title="development-app",
    description="backstage dev",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "development-app",
        "status": "running",
        "message": "Welcome to development-app"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }
