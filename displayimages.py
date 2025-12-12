import imageio.v2 as iio
import matplotlib.pyplot as plt

images = [
    "G:/cartoon_kid_.png",
    "G:/beautiful-flowers-rose.jpg",
    "G:/dog.jpeg"
]

for path in images:
    img = iio.imread(path)
    plt.imshow(img)
    plt.axis("off")
    plt.title(path)
    plt.show()
