import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from server.endpoints import chat_router

app = FastAPI(
    title="PolicyGPT API",
    version="1.0.0",
    description="Agentic AI HR Assistant API - Production Ready",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Demo API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Include routers
app.include_router(chat_router, prefix="/api/v1", tags=["Chat"])

def main():
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 8000))
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    main()