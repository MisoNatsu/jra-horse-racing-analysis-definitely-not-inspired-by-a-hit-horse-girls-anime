# Untuk tugas doang :D

# JRA 2024 Horse Racing - Win Odds Distribution Analysis

Proyek ini bertujuan untuk menganalisis dan memvalidasi bentuk distribusi probabilitas dari variabel kontinu **Odds Kemenangan (`win_odds`)** menggunakan dataset hasil pacuan kuda *Japan Racing Association* (JRA) tahun 2024.

---

## 📌 Deskripsi Data
* **Sumber Data:** Dataset Pacuan Kuda JRA 2024 (Kaggle)
* **Ukuran Dataset:** 12.060 observasi valid (setelah pembersihan 41 data kosong / 0,34%)
* **Variabel Utilitas:** `win_odds`

### Ringkasan Statistik Deskriptif
* **Jumlah Observasi ($n$):** 12.060
* **Nilai Minimum:** 1,10
* **Nilai Maksimum:** 948,50
* **Rata-rata (*Mean*):** 80,34
* **Nilai Tengah (*Median*):** 26,10
* **Standar Deviasi:** 122,96

---

## 📊 Hasil Uji Distribution Fitting (AIC)

Pengujian dilakukan terhadap 5 kandidat distribusi probabilitas (*Log-Normal, Gamma, Weibull, Exponential,* dan *Normal*). Model dievaluasi menggunakan kriteria **Akaike Information Criterion (AIC)**:

| Distribusi | Nilai AIC | Evaluasi Kecocokan Relatif |
| :--- | :--- | :--- |
| **Log-Normal** | **124.308** | **Best Fit (Relatif Terbaik)** |
| Gamma | 125.589 | Cocok |
| Weibull | 125.834 | Cukup Cocok |
| Exponential | 129.588 | Kurang Cocok |
| Normal | 150.289 | Paling Tidak Cocok |

> **Kesimpulan Utama:** Distribusi **Log-Normal** terbukti secara matematis merupakan model relatif terbaik dibanding kandidat lainnya karena memiliki nilai AIC paling rendah dengan keunggulan yang signifikan ($\Delta\text{AIC} > 10$).

---

## 🖼️ Visualisasi Histogram

![Distribusi Win Odds JRA 2024](jra_win_odds_dist.png)

---

## 🔍 Evaluasi Metodologi & Batasan Analisis (*Critical Review*)

1. **Provenans Data (Data Provenance):** Data berasal dari agregasi pihak ketiga (Kaggle), bukan API resmi JRA. Validitas bergantung pada kurasi *uploader*.
2. **Karakteristik Uji Kolmogorov-Smirnov (KS-Test):** Meskipun Log-Normal unggul secara relatif (AIC), uji KS memberikan p-value $< 0,05$ (menolak $H_0$ absolut). Hal ini dikarenakan pada ukuran sampel besar ($n > 12.000$), uji KS memiliki *power* yang sangat tinggi sehingga deviasi kecil dari distribusi teoritis akan terdeteksi signifikan. Oleh karena itu, kriteria AIC lebih tepat digunakan untuk perbandingan relatif antar-model.
3. **Penanganan Outlier & Pembatasan Visual:** Sumbu-X pada histogram dibatasi hingga batas `300` agar visualisasi kurva utama tetap terfokus. Terdapat sekitar **7,2% data ($> 300$)** yang berada pada ekor panjang (*long-tail*) dan terpotong secara visual, namun seluruh data penuh tetap disertakan dalam perhitungan kriteria AIC.

---

## 🛠️ Cara Menjalankan Kode

1. Pastikan Python 3.x dan *library* yang dibutuhkan sudah terinstal:
   ```bash
   pip install pandas numpy matplotlib scipy