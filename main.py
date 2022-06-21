import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from routers.v1 import platform_crowd_level as pcl

HOST = "0.0.0.0"
PORT = 8080

app = FastAPI()

apiv1 = FastAPI()
apiv1.include_router(pcl.router)

app.mount("/api/v1", apiv1)


@app.get("/")
def read_root():
    return RedirectResponse("/docs")


@apiv1.get("/")
def read_sub(request: Request):
    root_path = request.scope.get("root_path")
    return RedirectResponse(f"{root_path}/docs")


uvicorn.run(app, host=HOST, port=PORT, server_header=False)