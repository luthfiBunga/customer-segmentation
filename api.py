
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

# =====================================
# 1. MEMUAT MODEL DAN PREPROCESSOR
# =====================================

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

kmeans = joblib.load(
    BASE_DIR / "model" / "kmeans_model.pkl"
)

preprocessor = joblib.load(
    BASE_DIR / "model" / "preprocessor.pkl"
)

# =====================================
# 2. MEMBUAT APLIKASI FASTAPI
# =====================================

app = FastAPI(
    title="Customer Segmentation API",
    description="API untuk segmentasi pelanggan UMKM",
    version="1.0.0"
)


# =====================================
# 3. NAMA SEGMEN PELANGGAN
# =====================================

nama_cluster = {
    0: "Pelanggan Loyal dan Aktif",
    1: "Pelanggan Tidak Aktif",
    2: "Pelanggan Sensitif terhadap Promo",
    3: "Pelanggan Bernilai Belanja Tinggi"
}


# =====================================
# 4. REKOMENDASI PROMO
# =====================================

rekomendasi_promo = {
    0: "Berikan reward loyalitas, poin membership, dan penawaran eksklusif.",
    1: "Kirim voucher reaktivasi agar pelanggan tertarik berbelanja kembali.",
    2: "Berikan promo terarah, bundling produk, atau diskon minimum pembelian.",
    3: "Tawarkan produk premium, produk pelengkap, dan layanan eksklusif."
}


# =====================================
# 5. STRUKTUR DATA INPUT PELANGGAN
# =====================================

class DataPelanggan(BaseModel):
    umur: float | None = None
    kecamatan: str | None = None
    channel_utama: str | None = None
    metode_bayar: str | None = None
    kategori_favorit: str | None = None

    jumlah_transaksi_6bln: float | None = Field(default=None, ge=0)
    total_belanja_rp: float | None = Field(default=None, ge=0)
    hari_sejak_transaksi_terakhir: float | None = Field(default=None, ge=0)
    persen_pakai_promo: float | None = Field(default=None, ge=0, le=100)
    rating_rata: float | None = Field(default=None, ge=1, le=5)


# =====================================
# 6. ENDPOINT HALAMAN UTAMA
# =====================================

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Customer Segmentation API aktif!"
    }


# =====================================
# 7. ENDPOINT PREDIKSI SEGMEN PELANGGAN
# =====================================

@app.post("/predict")
def predict(data: DataPelanggan):
    try:
        # Mengubah input menjadi DataFrame
        input_data = pd.DataFrame([data.model_dump()])

        # Melakukan preprocessing
        data_processed = preprocessor.transform(input_data)

        # Melakukan prediksi cluster
        hasil_cluster = int(
            kmeans.predict(data_processed)[0]
        )

        # Mengambil nama segmen
        hasil_segmen = nama_cluster[hasil_cluster]

        # Mengambil rekomendasi promo
        hasil_rekomendasi = rekomendasi_promo[hasil_cluster]

        # Mengembalikan hasil prediksi
        return {
            "status": "success",
            "cluster": hasil_cluster,
            "segmen": hasil_segmen,
            "rekomendasi_promo": hasil_rekomendasi
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Terjadi kesalahan saat prediksi: {str(e)}"
        )
