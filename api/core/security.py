from pathlib import Path
from io import BytesIO

from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

ALLOWED_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp"
}

MAX_SIZE = 10 * 1024 * 1024  # 10 MB


async def validate_image(image: UploadFile) -> Image.Image:

    ext = Path(image.filename).suffix.lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Format gambar tidak didukung."
        )

    if image.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail="File harus berupa JPG, PNG, atau WEBP."
        )

    content = await image.read()

    if len(content) > MAX_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Ukuran gambar maksimal 10 MB."
        )

    try:
        img = Image.open(BytesIO(content))
        return img

    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="File bukan gambar yang valid."
        )