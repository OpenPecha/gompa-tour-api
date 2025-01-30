from fastapi import FastAPI
from pydantic import BaseModel
from prisma import Prisma
import uvicorn
import os
from Config.connection import prisma_connection
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from routes.check import router as check_router
from routes.contact import router as contact_router
from routes.language import router as language_router
from routes.gonpa import router as gonpa_router
from routes.statue import router as statue_router
from routes.user import router as user_router
from routes.festival import router as festival_router
from routes.pilgrim import router as pilgrim_router

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma_connection.connect()
    yield
    await prisma_connection.disconnect()

load_dotenv(override=True)
app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


app.include_router(check_router,prefix='/check',tags=["check"])
app.include_router(gonpa_router,prefix='/gonpa',tags=["gonpa"])
app.include_router(language_router,prefix='/language',tags=["language"])
app.include_router(contact_router,prefix='/contact',tags=["contact"])
app.include_router(statue_router,prefix='/statue',tags=["statue"])
app.include_router(user_router,prefix='/user',tags=["user"])
app.include_router(festival_router,prefix='/festival',tags=["festival"])
app.include_router(pilgrim_router,prefix='/pilgrim',tags=["pilgrim"])

def get_port():
    """Retrieve the PORT from environment variables, defaulting to 8000 if not set."""
    port = os.getenv("PORT", 8000)  # Default to 8000 if PORT is not set
    try:
        return int(port)  # Ensure the port is an integer
    except ValueError:
        raise ValueError(f"Invalid PORT value: {port}. It must be an integer.")

if __name__ == "__main__":
    port = get_port()
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)