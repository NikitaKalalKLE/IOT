import imageio.v2 as iio
import os

image_paths = [
    "G:/cartoon_kid_.png",
    "G:/beautiful-flowers-rose.jpg",
    "G:/dog.jpeg"
]

image_info_list = []

for path in image_paths:
    img = iio.imread(path)
    height, width = img.shape[:2]   # shape → (H, W, Channels)

    info = {
        "filename": os.path.basename(path),
        "width": width,
        "height": height
    }

    image_info_list.append(info)

# print the info list
for item in image_info_list:
    print(item)
