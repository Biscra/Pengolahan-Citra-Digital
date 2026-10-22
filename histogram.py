
import imageio.v3 as iio
import numpy as np
import matplotlib.pyplot as plt

# 1. Membaca gambar RGB
gambar = iio.imread("wowo.jpeg")

# Pastikan gambar memiliki 3 channel warna
gambar = gambar[:, :, :3]

# 2. Mengubah RGB menjadi grayscale
grayscale = (
    0.299 * gambar[:, :, 0] +
    0.587 * gambar[:, :, 1] +
    0.114 * gambar[:, :, 2]
).astype(np.uint8)

# 3. Menghitung histogram intensitas 0-255
histogram = np.bincount(grayscale.ravel(), minlength=256)

# 4. Menampilkan jumlah piksel setiap intensitas
print("Jumlah total piksel:", grayscale.size)
print("\nHistogram intensitas piksel:")

for intensitas in range(256):
    print(f"Intensitas {intensitas}: {histogram[intensitas]} piksel")

# 5. Menentukan intensitas yang paling dominan
intensitas_dominan = np.argmax(histogram)
jumlah_dominan = histogram[intensitas_dominan]

print("\nIntensitas paling dominan:", intensitas_dominan)
print("Jumlah piksel dominan:", jumlah_dominan)

# 6. Menampilkan gambar RGB, grayscale, dan histogram
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(gambar)
plt.title("Gambar RGB")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(grayscale, cmap="gray", vmin=0, vmax=255)
plt.title("Gambar Grayscale")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.bar(range(256), histogram, width=1.0)
plt.title("Histogram Grayscale")
plt.xlabel("Intensitas Piksel (0-255)")
plt.ylabel("Jumlah Piksel")
plt.xlim(0, 255)

plt.tight_layout()
plt.savefig("hasil_histogram.png", dpi=150)
plt.show()
