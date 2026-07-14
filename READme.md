# 🐱 Cat Skin Disease API

REST API untuk mendeteksi penyakit kulit pada kucing menggunakan model EfficientNetB0.

Repository ini hanya berisi backend production yang digunakan untuk melakukan inferensi model Machine Learning.

---

## Features

- REST API dengan FastAPI
- Image Classification
- PostgreSQL
- Swagger UI
- Prediction History

---

## Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- TensorFlow
- Uvicorn

---

## Endpoint

| Method | Endpoint | Deskripsi        |
| ------ | -------- | ---------------- |
| GET    | /        | API Status       |
| GET    | /health  | Health Check     |
| POST   | /predict | Prediksi Gambar  |
| GET    | /history | Riwayat Prediksi |

---

## Run

pip install -r requirements.txt

uvicorn api.app:app --reload
