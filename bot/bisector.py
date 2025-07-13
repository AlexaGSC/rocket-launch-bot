import io
from typing import List, NamedTuple, Text
from urllib.parse import quote, urljoin

from httpx import Client
from PIL import Image

API_BASE = "https://framex-develop-amzw3.ondigitalocean.app/api/"
VIDEO_NAME = "Falcon Heavy Test Flight (Hosted Webcast)-wbSwFU6tY1c"

class Size(NamedTuple):
    width: int
    height: int

class Color(NamedTuple):
    r: int
    g: int
    b: int

class Video(NamedTuple):
    name: Text
    width: int
    height: int
    frames: int
    frame_rate: List[int]
    url: Text
    first_frame: Text
    last_frame: Text

class FrameX:
    def __init__(self):
        self.client = Client(timeout=30)

    def video(self, video: Text) -> Video:
        r = self.client.get(urljoin(API_BASE, f"video/{quote(video)}/"))
        r.raise_for_status()
        return Video(**r.json())

    def video_frame(self, video: Text, frame: int) -> bytes:
        r = self.client.get(
            urljoin(API_BASE, f'video/{quote(video)}/frame/{quote(str(frame))}/')
        )
        r.raise_for_status()
        return r.content

class FrameXBisector:
    def __init__(self, name: str):
        self.api = FrameX()
        self.video = self.api.video(name)
        self._index = 0
        self.image_data = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, v):
        self._index = v
        self.image_data = self.api.video_frame(self.video.name, v)

    @property
    def count(self):
        return self.video.frames

def bisect(n, mapper, tester):
    if n < 1:
        raise ValueError("Cannot bisect an empty array")

    left = 0
    right = n - 1

    while left + 1 < right:
        mid = int((left + right) / 2)
        val = mapper(mid)
        if tester(val):
            right = mid
        else:
            left = mid

    return mapper(right)
