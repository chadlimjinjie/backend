from fastapi import APIRouter
import requests
from javascript import require

cron = require("node-cron")

pcl_list = []
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
    print("Updating PCL...")
    global pcl_list
    pcl_list = []
    for train_line in lines_shorthand_list:
        url = f"http://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine={train_line}"

        response = requests.get(url, headers=headers)
        response_data = response.json()
        # print(response_data)
        value = response_data.get("value")
        pcl_list.append(value)
    # print(pcl_list)


for train_line in lines_shorthand_list:
    url = f"http://datamall2.mytransport.sg/ltaodataservice/PCDRealTime?TrainLine={train_line}"

    response = requests.get(url, headers=headers)
    response_data = response.json()
    # print(response_data)
    value = response_data.get("value")
    pcl_list.append(value)
cron.schedule('*/3 * * * *', lambda cb: update_pcl())
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
    for i in range(len(lines_shorthand_list)):
        if train_line == lines_shorthand_list[i]:
            return pcl_list[i]


@router.get("/all")
def platform_crowd_level_all():
    # global pcl_list
    return pcl_list


@router.get("/{station_code}")
def station_crowd_level(station_code: str):
    for line in pcl_list:
        for station in line:
            if station["Station"] == station_code:
                return station
