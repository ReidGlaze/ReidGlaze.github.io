"""Embed local images into the built HTML so they get encrypted with the pages.

Usage: python3 tools/inline-images.py _site

Each /assets/images/* reference in an HTML file is replaced with a compressed
WebP data URI, image popup links and social preview tags pointing at those
files are removed, and the assets/images folder is deleted from the build.
"""

import base64
import io
import pathlib
import re
import shutil
import sys

from PIL import Image

MAX_WIDTH = 1600
QUALITY = 80

site = pathlib.Path(sys.argv[1])
images_dir = site / "assets" / "images"
cache = {}


def data_uri(name):
    if name not in cache:
        with Image.open(images_dir / name) as img:
            if img.width > MAX_WIDTH:
                img = img.resize((MAX_WIDTH, round(img.height * MAX_WIDTH / img.width)))
            buf = io.BytesIO()
            img.save(buf, "WEBP", quality=QUALITY)
        cache[name] = "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()
    return cache[name]


IMAGE = r'(?:https://reidglaze\.github\.io)?/assets/images/([^"]+)'

for page in site.rglob("*.html"):
    html = page.read_text(encoding="utf-8")
    # Social preview tags would point at deleted files.
    html = re.sub(r'<meta[^>]*content="' + IMAGE + r'"[^>]*>', "", html)
    html = re.sub(r'"image":"' + IMAGE + r'",', "", html)
    # Turn image popup links into plain wrappers.
    html = re.sub(r'(<a[^>]*?) href="' + IMAGE + r'"', r"\1", html)
    html = re.sub(r'(<a[^>]*class="[^"]*?)\bpopup ', r"\1", html)
    html = re.sub(r'src="' + IMAGE + r'"', lambda m: f'src="{data_uri(m.group(1))}"', html)
    page.write_text(html, encoding="utf-8")

shutil.rmtree(images_dir)
print(f"Embedded {len(cache)} images")
