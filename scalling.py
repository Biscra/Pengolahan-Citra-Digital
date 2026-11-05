
import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("roni.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Scaling 0.5 (memperkecil)
hasil_kecil = cv2.resize(
    img, None, fx=0.5, fy=0.5,
    interpolation=cv2.INTER_LINEAR
)

# Scaling 2 (memperbesar)
hasil_besar = cv2.resize(
    img, None, fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Menampilkan informasi ukuran
print("Ukuran gambar asli:", img.shape)
print("Ukuran Scaling 0.5:", hasil_kecil.shape)
print("Ukuran Scaling 2:", hasil_besar.shape)

# Menampilkan gambar
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hasil_kecil)
plt.title("Scaling 0.5")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil_besar)
plt.title("Scaling 2")
plt.axis("off")

plt.tight_layout()
plt.show()

# Menyimpan hasil
cv2.imwrite("scaling_05.jpg",
            cv2.cvtColor(hasil_kecil, cv2.COLOR_RGB2BGR))

cv2.imwrite("scaling_2.jpg",
            cv2.cvtColor(hasil_besar, cv2.COLOR_RGB2BGR))
