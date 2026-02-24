from PIL import Image


def resize_image(img):
    w, h = img.size
    longer_edge = w if w > h else h
    if longer_edge > 1568:
        max_size = (1568, 1568)
        img.thumbnail(max_size, Image.LANCZOS)

    return img
