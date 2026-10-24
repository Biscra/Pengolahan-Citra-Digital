import imageio.v3 as iio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Membaca gambar
gambar = iio.imread("wowo.jpeg")

# Mengubah gambar menjadi grayscale
if gambar.ndim == 3:
    gambar = np.dot(
        gambar[:, :, :3],
        [0.299, 0.587, 0.114]
    )

gambar = gambar.astype(np.uint8)

# Mengurangi noise
filter_gambar = ndimage.gaussian_filter(
    gambar.astype(float), sigma=0.7
)

filter_gambar = np.clip(
    filter_gambar, 0, 255
).astype(np.uint8)

# Meningkatkan kontras dengan Histogram Equalization
histogram = np.bincount(
    filter_gambar.ravel(), minlength=256
)

cdf = histogram.cumsum()
cdf_min = cdf[cdf > 0][0]
total = filter_gambar.size

hasil = (
    (cdf[filter_gambar] - cdf_min)
    / (total - cdf_min) * 255
)

hasil = np.clip(hasil, 0, 255).astype(np.uint8)

# Menyimpan gambar hasil
iio.imwrite("hasil_peningkatan.png", hasil)

# Menampilkan perbandingan gambar
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(gambar, cmap="gray", vmin=0, vmax=255)
plt.title("Citra Awal")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil, cmap="gray", vmin=0, vmax=255)
plt.title("Citra Setelah Peningkatan")
plt.axis("off")

plt.tight_layout()
plt.savefig("perbandingan_citra.png")
plt.show()