import imageio.v2 as iio
import matplotlib.pyplot as plt

jpg_file =r"G:/cartoon_kid_.png"
img = iio.imread(jpg_file)

plt.imshow(img)
plt.axis('off')
plt.show()