import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routers.v1 import disney_plus
from routers.v1 import platform_crowd_level as pcl
from routers.v1 import taxi
from routers.v1 import twitter
from routers.v1 import discord
from routers.v1 import youtube

HOST = "0.0.0.0"
PORT = os.getenv("PORT") or 8080
origins = [
    "*"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

apiv1 = FastAPI()
apiv2 = FastAPI()

apiv1.include_router(discord.router)
apiv1.include_router(disney_plus.router)
apiv1.include_router(pcl.router)
apiv1.include_router(taxi.router)
apiv1.include_router(twitter.router)
apiv1.include_router(youtube.router)

app.mount("/api/v1", apiv1)
app.mount("/api/v2", apiv2)


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@apiv1.get("/")
@apiv2.get("/")
def read_sub(request: Request):
    root_path = request.scope.get("root_path")
    return RedirectResponse(f"{root_path}/docs")


uvicorn.run(app, host=HOST, port=PORT, server_header=False)