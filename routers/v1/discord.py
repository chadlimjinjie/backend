from fastapi import APIRouter
import requests
import json

router = APIRouter(
    prefix="/discord",
    tags=["discord"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("/webhook")
def discord_webhook(body: dict):
    embeds = body["embeds"]
    if embeds:
        body["embeds"] = json.loads(f"[{embeds}]".replace('}\n{', '},{'))
    res = requests.post(
        "https://discord.com/api/webhooks/954685496573952000/13lqmz5moC3y_ARHc0KEjtaee2tnAugY7r2E356-S_KHfRonEJbDgTcJoMP2E9tE1AvP",
        json=body)
    print(res.json())
    return 200
