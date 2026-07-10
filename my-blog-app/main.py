import os
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

app = FastAPI()

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Welcome to your Blog API",
        "database": DATABASE_URL.split("@")[-1]  # Hide credentials
    }

@app.get("/health")
async def health_check():
    try:
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
