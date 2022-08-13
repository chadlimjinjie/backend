from fastapi import APIRouter
from fastapi.responses import FileResponse
from pytube import YouTube
import unicodedata
import re
import os


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD',
                                      value).encode('ascii',
                                                    'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


router = APIRouter(
    prefix="/youtube",
    tags=["YouTube"],
    responses={404: {
        "description": "Not found"
    }},
)

prev_mp3_title = ""


@router.get("/mp3")
def to_mp3(link: str):
    global prev_mp3_title
    if prev_mp3_title != "":
        os.remove(prev_mp3_title)
    yt = YouTube(link)
    try:
        print(yt.title)
        # yt.title = slugify(yt.title)
        yt.streams.first().download()
        os.rename(f'{yt.title}.3gpp', f'{yt.title}.mp3')
        prev_mp3_title = yt.title + ".mp3"
        return FileResponse(f'{yt.title}.mp3', media_type="application/octet-stream", filename=prev_mp3_title)
    except Exception as e:
        print(e)


prev_mp4_title = ""


@router.get("/mp4")
def to_mp4(link: str):
    global prev_mp4_title
    if prev_mp4_title != "":
        os.remove(prev_mp4_title)
    yt = YouTube(link)
    try:
        print(yt.title)
        # yt.title = slugify(yt.title)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download()
        prev_mp4_title = yt.title + ".mp4"
        return FileResponse(f'{yt.title}.mp4', media_type="application/octet-stream", filename=prev_mp4_title)
    except Exception as e:
        print(e)
