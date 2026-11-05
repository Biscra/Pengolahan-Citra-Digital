
import cv2
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("roni.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

tinggi, lebar = img.shape[:2]

# Fungsi rotasi
def rotasi(gambar, sudut):
    tinggi, lebar = gambar.shape[:2]
    pusat = (lebar // 2, tinggi // 2)

    M = cv2.getRotationMatrix2D(pusat, sudut, 1.0)

    cos = abs(M[0, 0])
    sin = abs(M[0, 1])

    lebar_baru = int((tinggi * sin) + (lebar * cos))
    tinggi_baru = int((tinggi * cos) + (lebar * sin))

    M[0, 2] += (lebar_baru / 2) - pusat[0]
    M[1, 2] += (tinggi_baru / 2) - pusat[1]

    hasil = cv2.warpAffine(
        gambar, M, (lebar_baru, tinggi_baru)
    )

    return hasil

# Melakukan rotasi
rotasi_45 = rotasi(img, 45)
rotasi_90 = rotasi(img, 90)
rotasi_180 = rotasi(img, 180)

# Menampilkan hasil
plt.figure(figsize=(15, 8))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Citra Asli")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(rotasi_45)
plt.title("Rotasi 45 Derajat")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(rotasi_90)
plt.title("Rotasi 90 Derajat")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(rotasi_180)
plt.title("Rotasi 180 Derajat")
plt.axis("off")

plt.tight_layout()
plt.show()

# Menyimpan hasil
cv2.imwrite("rotation_45.jpg",
            cv2.cvtColor(rotasi_45, cv2.COLOR_RGB2BGR))
cv2.imwrite("rotation_90.jpg",
            cv2.cvtColor(rotasi_90, cv2.COLOR_RGB2BGR))
cv2.imwrite("rotation_180.jpg",
            cv2.cvtColor(rotasi_180, cv2.COLOR_RGB2BGR))
