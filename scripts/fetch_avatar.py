#!/usr/bin/env python3
"""Download the profile avatar and prepare it as grayscale input for the ASCII portrait."""
import os
from io import BytesIO

import requests
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
USER = os.environ.get("GH_PROFILE_USER", "themanvendra00")
OUT_PATH = os.path.join(HERE, "..", "source-prepped.png")
URL = f"https://github.com/{USER}.png?size=512"

response = requests.get(URL, headers={"User-Agent": "profile-readme-bot/1.0"}, timeout=30)
response.raise_for_status()

with Image.open(BytesIO(response.content)) as avatar:
    avatar.convert("L").save(OUT_PATH)

print(f"wrote {OUT_PATH} from {USER}'s GitHub avatar")
