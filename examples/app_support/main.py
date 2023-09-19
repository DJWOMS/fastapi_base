import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from src.routers.support import router as support_router


def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.project_name,
        version=settings.version
    )
    application.include_router(support_router)
    return application


app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
