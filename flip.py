
import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("roni.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Horizontal Flip
horizontal = cv2.flip(img, 1)

# Vertical Flip
vertical = cv2.flip(img, 0)

# Menampilkan hasil
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(horizontal)
plt.title("Horizontal Flip")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(vertical)
plt.title("Vertical Flip")
plt.axis("off")

plt.tight_layout()
plt.show()

# Menyimpan hasil
cv2.imwrite(
    "horizontal_flip.jpg",
    cv2.cvtColor(horizontal, cv2.COLOR_RGB2BGR)
)

cv2.imwrite(
    "vertical_flip.jpg",
    cv2.cvtColor(vertical, cv2.COLOR_RGB2BGR)
)
