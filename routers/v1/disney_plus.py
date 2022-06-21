import os
from fastapi import APIRouter, HTTPException
import requests
import json
from datetime import datetime

with open(os.path.join(os.getcwd(), "static", "series.json")) as f:
    series = json.load(f)

router = APIRouter(
    prefix="/disney",
    tags=["disney"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("")
async def read_series_list():
    return series


@router.get("/{series_id}")
async def read_series_id(series_id: str):
    videos = []
    episode_list = []
    series_region = series["SG"]

    if series_id not in series_region.keys():
        raise HTTPException(status_code=404, detail="Item not found")

    series_region_dmcepisodes = series_region[series_id].get("DmcEpisodes")
    series_region_dmcseriesbundle = series_region[series_id].get(
        "DmcSeriesBundle")
    series_region_dmcvideobundle = series_region[series_id].get(
        "DmcVideoBundle")

    if series_region_dmcepisodes:
        response = requests.get(series_region_dmcepisodes)
        response_data = response.json()

        dmc_episodes = response_data["data"]["DmcEpisodes"]
        print(dmc_episodes)

        videos = dmc_episodes["videos"]

    elif series_region_dmcvideobundle:
        response = requests.get(series_region_dmcvideobundle)
        response_data = response.json()

        dmc_videobundle = response_data["data"]["DmcVideoBundle"]
        print(dmc_videobundle)

    if len(videos) == 0 and series_region_dmcseriesbundle:
        response = requests.get(series_region_dmcseriesbundle)
        response_data = response.json()

        dmc_series_bundle = response_data["data"]["DmcSeriesBundle"]

        promoLabels = dmc_series_bundle["promoLabels"][0]
        sunrise = promoLabels["sunrise"]
        sunrise = datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S%z")
        sunrise = sunrise.strftime("%d/%m/%Y, %H:%M:%S")

        sunset = promoLabels["sunset"]
        sunset = datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
        sunset = sunset.strftime("%d/%m/%Y, %H:%M:%S")

        print(sunrise, sunset)

        return f"Coming Soon {sunset}"

    for video in videos:

        ep_title = video["text"]["title"]["full"]["program"]["default"][
            "content"]
        ep_runtime_mins = video["mediaMetadata"]["runtimeMillis"] / 60000
        # print(ep_title, ep_runtime_mins)

        episode_list.append({
            "title": ep_title,
            "runtimeMins": ep_runtime_mins
        })

    return episode_list

    # if len(videos) == 0:
    #     promoLabels = dmcSeriesBundle["promoLabels"][0]
    #     sunrise = promoLabels["sunrise"]
    #     sunrise = datetime.strptime(sunrise, "%Y-%m-%dT%H:%M:%S%z")
    #     sunrise = sunrise.strftime("%d/%m/%Y, %H:%M:%S")

    #     sunset = promoLabels["sunset"]
    #     sunset = datetime.strptime(sunset, "%Y-%m-%dT%H:%M:%S%z")
    #     sunset = sunset.strftime("%d/%m/%Y, %H:%M:%S")

    #     print(sunrise, sunset)

    #     raise HTTPException(status_code=200, detail=f"Coming Soon {sunset}")
