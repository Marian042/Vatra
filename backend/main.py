from fastapi import FastAPI

app = FastAPI(
    title="VATRA",
    description="Local Smart Home Control System",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "VATRA",
        "status": "online",
        "message": "Your home. Under control.",
    }


@app.get("/health")
async def health():
    return {"status": "healthy"}