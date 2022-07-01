import os
from fastapi import APIRouter, HTTPException
import requests
import json
from datetime import datetime
from clients.twitter_client import twitter_client

router = APIRouter(
    prefix="/twitter",
    tags=["twitter"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("")
async def root():
    twitter_client.create_tweet(text="Hello, world!")
    return {}
