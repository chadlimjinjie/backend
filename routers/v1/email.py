from fastapi import APIRouter
from clients.yagmail_client import send_raw_email

router = APIRouter(
    prefix="/email",
    tags=["Email"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.post("")
async def email(to_email: str, subject: str, text: str):
    send_raw_email(to_email, subject, text)
    return {}
