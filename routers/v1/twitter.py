import os
from fastapi import APIRouter, HTTPException
import requests
import json
from datetime import datetime
from clients.twitter_client import twitter_client
from pydantic import BaseModel

router = APIRouter(
    prefix="/twitter",
    tags=["twitter"],
    responses={404: {
        "description": "Not found"
    }},
)


class Tweet(BaseModel):
    text: str


@router.post("")
async def create_tweet(tweet: Tweet):
    tweet = twitter_client.create_tweet(text=tweet.text)
    return tweet
