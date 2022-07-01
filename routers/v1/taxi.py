from fastapi import APIRouter
from fastapi.websockets import WebSocket
import requests
from scipy import spatial

# airports = [(10,10),(20,20),(30,30),(40,40)]
# tree = spatial.KDTree(airports)
# tree.query([(21,21)])

router = APIRouter(
    prefix="/taxi",
    tags=["taxi"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # data = await websocket.receive_text()
        # await websocket.send_text(f"Message text was: {data}")
        await websocket.send_text("taxi")


@router.get("")
async def list_of_taxi_coordinate():
    res = requests.get(
        "https://api.data.gov.sg/v1/transport/taxi-availability")
    res_data = res.json()
    return res_data


@router.get("/nearest")
async def nearest_taxi_coordinate(long: float, lat: float):

    res = requests.get(
        "https://api.data.gov.sg/v1/transport/taxi-availability")
    res_data = res.json()
    taxis = list(map(tuple,
                     res_data["features"][0]["geometry"]["coordinates"]))
    # print(taxis)
    tree = spatial.KDTree(taxis)
    nearest = tree.query([(long, lat)])
    # print(nearest)
    distance = nearest[0].tolist()[0]
    coordinate = taxis[nearest[1].tolist()[0]]
    long = coordinate[0]
    lat = coordinate[1]
    return {"distance": distance, "coordinate": {"long": long, "lat": lat}}
