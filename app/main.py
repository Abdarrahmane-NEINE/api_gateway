from fastapi import FastAPI
from app.config import settings
from app.middlewares.logging import LoggingMiddleware
from app.routers import gateway, service1, service2
from app.routers.auth.verify import router as auth_verify_router
# FastAPI instance with metadata (OpenAPI docs)
app = FastAPI(
    title="API Gateway",
    description="A single entry point for routing, authentication, and monitoring of backend services.",
    version="1.0"
)

# Register custom middleware (SOLID: Single Responsibility - Logging concerns are isolated)
app.add_middleware(LoggingMiddleware)

# routers
app.include_router(gateway.router, prefix="/gateway", tags=["Gateway"])
app.include_router(auth_verify_router, prefix="/auth", tags=["Authentication"])
app.include_router(service1.router, prefix="/service1", tags=["Service1"])
app.include_router(service2.router, prefix="/service2", tags=["Service2"])

if __name__ == "__main__":
    import uvicorn
    # Uvicorn runs the application with auto-reload for development.
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
