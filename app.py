
import streamlit as st
import requests

# =====================================================
# 1. KONFIGURASI HALAMAN
# =====================================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://127.0.0.1:8000"

# =====================================================
# 2. DATA SEGMEN DAN REKOMENDASI
# =====================================================

segmen_info = {
    0: {
        "nama": "Pelanggan Loyal dan Aktif",
        "deskripsi": "Pelanggan dengan frekuensi transaksi tinggi dan aktivitas belanja yang aktif.",
        "promo": "Berikan reward loyalitas, poin membership, dan penawaran eksklusif.",
        "warna": "#DCFCE7"
    },
    1: {
        "nama": "Pelanggan Tidak Aktif",
        "deskripsi": "Pelanggan dengan transaksi rendah dan sudah cukup lama tidak berbelanja.",
        "promo": "Kirim voucher reaktivasi agar pelanggan tertarik berbelanja kembali.",
        "warna": "#FEE2E2"
    },
    2: {
        "nama": "Pelanggan Sensitif terhadap Promo",
        "deskripsi": "Pelanggan yang memiliki kecenderungan tinggi menggunakan promosi.",
        "promo": "Berikan promo terarah, bundling produk, atau diskon minimum pembelian.",
        "warna": "#FEF3C7"
    },
    3: {
        "nama": "Pelanggan Bernilai Belanja Tinggi",
        "deskripsi": "Pelanggan dengan nilai belanja relatif tinggi meskipun frekuensi transaksi lebih rendah.",
        "promo": "Tawarkan produk premium, produk pelengkap, dan layanan eksklusif.",
        "warna": "#DBEAFE"
    }
}

# =====================================================
# 3. CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background-color: #F5F7FB;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}

.main-header {
    background: linear-gradient(135deg, #172554, #2563EB);
    padding: 32px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.main-header h1 {
    color: white;
    font-size: 34px;
    margin-bottom: 8px;
}

.main-header p {
    color: #DBEAFE;
    font-size: 16px;
    margin-bottom: 0;
}

.section-card {
    background-color: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #E2E8F0;
    margin-bottom: 15px;
}

.result-card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #E2E8F0;
    margin-top: 20px;
}

div.stButton > button {
    border-radius: 10px;
    font-weight: 600;
    min-height: 42px;
}

div[data-testid="stFormSubmitButton"] button {
    background-color: #1D4ED8;
    color: white;
    border-radius: 10px;
    font-weight: 600;
    min-height: 45px;
}

section[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    justify-content: flex-start;
    text-align: left;
    border: 1px solid #E2E8F0;
    background-color: #FFFFFF;
    color: #334155;
}

section[data-testid="stSidebar"] div.stButton > button:hover {
    border-color: #2563EB;
    color: #1D4ED8;
}

section[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
    background-color: #DBEAFE;
    border-color: #93C5FD;
    color: #1E40AF;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# 4. FUNGSI NAVIGASI
# =====================================================

if "menu" not in st.session_state:
    st.session_state["menu"] = "🏠 Dashboard"


def pindah_halaman(halaman):
    st.session_state["menu"] = halaman


# =====================================================
# 5. SIDEBAR
# =====================================================

with st.sidebar:

    st.title("📊 Customer Insight")
    st.caption("UMKM Bakery & Coffee Shop")

    st.divider()

    st.markdown("### MENU NAVIGASI")

    menu_items = [
        "🏠 Dashboard",
        "👥 Segmentasi Pelanggan",
        "🎯 Rekomendasi Promo"
    ]

    for halaman in menu_items:
        st.button(
            halaman,
            key=f"nav_{halaman}",
            use_container_width=True,
            type="primary" if st.session_state["menu"] == halaman else "secondary",
            on_click=pindah_halaman,
            args=(halaman,)
        )

    menu = st.session_state["menu"]

    st.divider()

    st.markdown("### INFORMASI MODEL")
    st.caption("Algoritma: K-Means Clustering")
    st.caption("Jumlah cluster: 4")
    st.caption("Framework: FastAPI + Streamlit")

    st.divider()

    st.caption("Customer Segmentation Project")
    st.caption("UMKM Bandung")

# =====================================================
# 6. HEADER
# =====================================================

st.markdown("""
<div class="main-header">
    <h1>Customer Segmentation</h1>
    <p>
        Analisis pelanggan dan rekomendasi strategi pemasaran
        berbasis Machine Learning.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# 7. STATUS FASTAPI
# =====================================================

with st.container():

    try:
        response = requests.get(API_URL, timeout=3)

        if response.status_code == 200:
            st.success("🟢 Sistem FastAPI terhubung dan siap digunakan.")

        else:
            st.warning(
                f"FastAPI memberikan status {response.status_code}."
            )

    except requests.exceptions.RequestException:
        st.error(
            "🔴 FastAPI belum terhubung. "
            "Pastikan server FastAPI berjalan pada port 8000."
        )

# =====================================================
# 8. HALAMAN DASHBOARD
# =====================================================

if menu == "🏠 Dashboard":

    st.title("🏠 Dashboard Utama")

    st.write(
        "Selamat datang di Customer Segmentation Dashboard. "
        "Gunakan aplikasi ini untuk memahami karakteristik "
        "pelanggan dan menentukan strategi pemasaran."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Total Pelanggan",
            value="10.000"
        )

    with col2:
        st.metric(
            label="Jumlah Segmen",
            value="4"
        )

    with col3:
        st.metric(
            label="Algoritma",
            value="K-Means"
        )

    st.divider()

    st.subheader("Jelajahi Aplikasi")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.markdown("### 👥 Segmentasi Pelanggan")
            st.write(
                "Masukkan data pelanggan untuk mengetahui "
                "segmen berdasarkan model Machine Learning."
            )

            st.button(
                "Buka Segmentasi Pelanggan →",
                use_container_width=True,
                on_click=pindah_halaman,
                args=("👥 Segmentasi Pelanggan",)
            )

    with col2:
        with st.container(border=True):
            st.markdown("### 🎯 Rekomendasi Promo")
            st.write(
                "Lihat strategi promosi yang sesuai dengan "
                "karakteristik masing-masing segmen."
            )

            st.button(
                "Lihat Rekomendasi Promo →",
                use_container_width=True,
                on_click=pindah_halaman,
                args=("🎯 Rekomendasi Promo",)
            )

    st.divider()

    st.subheader("Tentang Proyek")

    st.write("""
    Proyek Customer Segmentation menggunakan algoritma
    K-Means untuk mengelompokkan pelanggan UMKM berdasarkan
    karakteristik demografis, transaksi, dan perilaku pembelian.

    Hasil segmentasi digunakan untuk membantu pemilik usaha
    menentukan strategi pemasaran yang lebih tepat sasaran.
    """)

# =====================================================
# 9. HALAMAN SEGMENTASI PELANGGAN
# =====================================================

elif menu == "👥 Segmentasi Pelanggan":

    st.title("👥 Segmentasi Pelanggan")

    st.write(
        "Masukkan informasi pelanggan di bawah ini untuk "
        "mengetahui kelompok pelanggan dan rekomendasi promonya."
    )

    st.info(
        "Isi kategori sesuai nilai yang digunakan dalam dataset "
        "training agar hasil encoding sesuai dengan model."
    )

    with st.form("form_prediksi"):

        st.subheader("1. Informasi Demografis")

        col1, col2 = st.columns(2)

        with col1:
            umur = st.number_input(
                "Umur pelanggan",
                min_value=0,
                max_value=120,
                value=27,
                step=1
            )

        with col2:
            kecamatan = st.text_input(
                "Kecamatan",
                placeholder="Contoh: bandung wetan"
            )

        st.divider()

        st.subheader("2. Informasi Transaksi")

        col1, col2 = st.columns(2)

        with col1:
            channel_utama = st.text_input(
                "Channel utama",
                placeholder="Masukkan sesuai dataset"
            )

            metode_bayar = st.text_input(
                "Metode pembayaran",
                placeholder="Masukkan sesuai dataset"
            )

            kategori_favorit = st.text_input(
                "Kategori favorit",
                placeholder="Masukkan sesuai dataset"
            )

        with col2:
            jumlah_transaksi = st.number_input(
                "Jumlah transaksi selama 6 bulan",
                min_value=0,
                value=10,
                step=1
            )

            total_belanja = st.number_input(
                "Total belanja (Rp)",
                min_value=0.0,
                value=500000.0,
                step=50000.0
            )

        st.divider()

        st.subheader("3. Perilaku Pelanggan")

        col1, col2 = st.columns(2)

        with col1:
            hari_terakhir = st.number_input(
                "Hari sejak transaksi terakhir",
                min_value=0,
                value=10,
                step=1
            )

            persen_promo = st.number_input(
                "Persentase penggunaan promo (%)",
                min_value=0.0,
                max_value=100.0,
                value=20.0,
                step=1.0
            )

        with col2:
            rating = st.number_input(
                "Rating rata-rata",
                min_value=1.0,
                max_value=5.0,
                value=4.0,
                step=0.1
            )

        st.divider()

        submit = st.form_submit_button(
            "🤖 Prediksi Segmen Pelanggan",
            use_container_width=True
        )

    # =================================================
    # 10. PROSES PREDIKSI KE FASTAPI
    # =================================================

    if submit:

        if not kecamatan.strip():
            st.warning("Silakan isi kecamatan pelanggan.")

        elif not channel_utama.strip():
            st.warning("Silakan isi channel utama pelanggan.")

        elif not metode_bayar.strip():
            st.warning("Silakan isi metode pembayaran.")

        elif not kategori_favorit.strip():
            st.warning("Silakan isi kategori favorit.")

        else:

            data_pelanggan = {
                "umur": umur,
                "kecamatan": kecamatan.strip(),
                "channel_utama": channel_utama.strip(),
                "metode_bayar": metode_bayar.strip(),
                "kategori_favorit": kategori_favorit.strip(),
                "jumlah_transaksi_6bln": jumlah_transaksi,
                "total_belanja_rp": total_belanja,
                "hari_sejak_transaksi_terakhir": hari_terakhir,
                "persen_pakai_promo": persen_promo,
                "rating_rata": rating
            }

            try:

                with st.spinner(
                    "Sedang menganalisis data pelanggan..."
                ):

                    hasil = requests.post(
                        f"{API_URL}/predict",
                        json=data_pelanggan,
                        timeout=15
                    )

                if hasil.status_code == 200:

                    hasil_json = hasil.json()

                    cluster = int(hasil_json["cluster"])

                    if cluster not in segmen_info:
                        st.error("Model mengembalikan cluster yang tidak dikenal.")

                    else:
                        informasi = segmen_info[cluster]

                        st.session_state["hasil_prediksi"] = {
                            "cluster": cluster,
                            "segmen": hasil_json["segmen"],
                            "promo": hasil_json["rekomendasi_promo"]
                        }

                else:

                    st.error(
                        f"Prediksi gagal. Status HTTP: {hasil.status_code}"
                    )

                    st.code(hasil.text)

            except requests.exceptions.RequestException as e:

                st.error(
                    "Tidak dapat menghubungi FastAPI. "
                    "Pastikan server API masih berjalan."
                )

                st.code(str(e))

            except (ValueError, KeyError) as e:

                st.error("Format hasil prediksi tidak sesuai.")

                st.code(str(e))

    # =================================================
    # 11. MENAMPILKAN HASIL PREDIKSI
    # =================================================

    if "hasil_prediksi" in st.session_state:

        hasil = st.session_state["hasil_prediksi"]

        cluster = hasil["cluster"]

        informasi = segmen_info[cluster]

        st.divider()

        st.subheader("🎉 Hasil Segmentasi Pelanggan")

        with st.container(border=True):

            st.success("Prediksi berhasil dilakukan!")

            st.markdown(
                f"### {hasil['segmen']}"
            )

            st.metric(
                label="Nomor Cluster",
                value=f"Cluster {cluster}"
            )

            st.write(informasi["deskripsi"])

            st.divider()

            st.markdown("### 🎯 Rekomendasi Promo")

            st.info(hasil["promo"])

# =====================================================
# 12. HALAMAN REKOMENDASI PROMO
# =====================================================

elif menu == "🎯 Rekomendasi Promo":

    st.title("🎯 Rekomendasi Strategi Promo")

    st.write(
        "Berikut rekomendasi strategi pemasaran "
        "berdasarkan empat segmen pelanggan hasil K-Means."
    )

    for cluster, informasi in segmen_info.items():

        with st.container(border=True):

            st.markdown(
                f"### Cluster {cluster} — {informasi['nama']}"
            )

            st.write(informasi["deskripsi"])

            st.markdown("**Rekomendasi strategi:**")

            st.info(informasi["promo"])

# =====================================================
# 13. FOOTER
# =====================================================

st.divider()

st.caption(
    "Customer Segmentation | K-Means Clustering | "
    "FastAPI + Streamlit"
)