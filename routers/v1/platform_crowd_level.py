from fastapi import APIRouter
import requests
from javascript import require

cron = require("node-cron")

pcl = []
headers = {"AccountKey": "ShcXnDanSKqJ53wy47unFg=="}
lines = {
    "CCL": "Circle Line",
    "CEL": "Circle Line Extension – BayFront, Marina Bay",
    "CGL": "Changi Extension – Expo, Changi Airport",
    "DTL": "Downtown Line",
    "EWL": "East West Line",
    "NEL": "North East Line",
    "NSL": "North South Line",
    "BPL": "Bukit Panjang LRT",
    "SLRT": "Sengkang LRT",
    "PLRT": "Punggol LRT",
}
lines_shorthand_list = lines.keys()


def update_pcl():
    global pcl
    pcl = []
    for train_line in lines_shorthand_list:
        url = f"http://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine={train_line}"

        response = requests.get(url, headers=headers)
        response_data = response.json()
        pcl.append(response_data)
    # print(pcl)


cron.schedule('*/2 * * * *', lambda cb: update_pcl())
'''
Train lines supported:
• CCL (for Circle Line)
• CEL (for Circle Line Extension – BayFront, Marina Bay)
• CGL (for Changi Extension – Expo, Changi Airport)
• DTL (for Downtown Line)
• EWL (for East West Line)
• NEL (for North East Line)
• NSL (for North South Line)
• BPL (for Bukit Panjang LRT)
• SLRT (for Sengkang LRT)
• PLRT (for Punggol LRT)
'''

router = APIRouter(
    prefix="/platform-crowd-level",
    tags=["MRT"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("")
def platform_crowd_level(train_line: str):
    url = f"http://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine={train_line}"

    response = requests.get(url, headers=headers)
    response_data = response.json()
    # print(response_data)

    return response_data


@router.get("/all")
def platform_crowd_level():
    return pcl
