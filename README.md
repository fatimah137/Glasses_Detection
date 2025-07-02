# Glasses_Detection
Aplikasi Web Deteksi Kacamata Menggunakan CNN

Proyek ini merupakan implementasi **deep learning** dengan model **Convolutional Neural Network (CNN)** untuk mengklasifikasikan apakah seseorang **menggunakan kacamata atau tidak** berdasarkan gambar wajah. Model dilatih menggunakan dataset gambar yang terbagi menjadi dua kelas: **glasses** (memakai kacamata) dan **no\_glasses** (tidak memakai kacamata).

Aplikasi ini dibangun dalam dua tahap:

1. **Training model CNN** di Google Colab menggunakan TensorFlow dan ImageDataGenerator untuk augmentasi data.
2. **Deploy ke aplikasi web** menggunakan framework **Streamlit**, sehingga pengguna dapat mengunggah gambar dan melihat hasil prediksi secara real-time.

---

## 🎯 **Fitur Utama:**

* Klasifikasi gambar wajah: *Dengan Kacamata* / *Tanpa Kacamata*
* Dukungan upload file gambar (JPG, PNG)
* Tampilan responsif dan sederhana berbasis web
* Berjalan secara lokal tanpa memerlukan server eksternal.

---

## 🛠️ **Teknologi yang Digunakan:**

* **Python**
* **TensorFlow / Keras**
* **Streamlit**
* **Pillow** (PIL) untuk manipulasi gambar
* **Google Colab** untuk pelatihan model

---

## 📌 Tujuan:

Proyek ini bertujuan untuk menerapkan konsep deep learning dalam pengolahan citra, khususnya untuk klasifikasi biner berbasis fitur visual (keberadaan kacamata pada wajah), serta mengintegrasikannya ke dalam aplikasi web interaktif.


