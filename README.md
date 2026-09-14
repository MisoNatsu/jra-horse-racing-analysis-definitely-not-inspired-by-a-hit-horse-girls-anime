# JRA 2024 Horse Racing - Win Odds Distribution Analysis

Proyek ini bertujuan untuk menganalisis dan memvalidasi bentuk distribusi probabilitas dari variabel kontinu **Odds Kemenangan (`win_odds`)** menggunakan dataset hasil pacuan kuda *Japan Racing Association* (JRA) tahun 2024.

---

## 📌 Deskripsi Data & Parameter Statistik

* **Sumber Data:** Dataset Pacuan Kuda JRA 2024 (Kaggle)
* **Variabel Utilitas:** `win_odds`

Berikut adalah ringkasan parameter statistik aktual untuk data *Win Odds*:
* **μ (Rata-rata) = 80,34**: Patokan nilai pusat secara matematis. Besarnya angka ini didorong oleh *outlier* ekstrem (kuda yang sangat tidak diunggulkan), mengingat mayoritas data sebenarnya menumpuk di odds yang jauh lebih kecil (median 26,10).
* **σ (Standar Deviasi) = 122,96**: Tingkat keragaman nilai odds. Nilai yang sangat besar menunjukkan variasi peluang kemenangan yang sangat ekstrem dan fluktuatif antar kuda.
* **σ² (Varians) = 15.118,39**: Ukuran sebaran data di sekitar rata-rata. Menegaskan bahwa sebaran data sangat berpencar dan memiliki ekor yang merentang sangat jauh dari titik pusatnya.
* **[a, b] (Batas Data) = [1,1 ; 948,5]**: Rentang nilai rasio imbal hasil (*Win Odds*) yang tercatat secara nyata. Batas bawah 1,1 menandakan kuda yang paling difavoritkan, sedangkan 948,5 adalah kuda *underdog* ekstrem.
* **N (Total Data) = 12.060**: Banyaknya catatan observasi valid yang digunakan dalam analisis (setelah *missing values* dikeluarkan).

---

## 📊 Hasil Uji Distribution Fitting (AIC)

Pengujian dilakukan terhadap 5 kandidat distribusi probabilitas. Model dievaluasi menggunakan kriteria **Akaike Information Criterion (AIC)**:

| Distribusi | Nilai AIC | Evaluasi Kecocokan Relatif |
| :--- | :--- | :--- |
| **Log-Normal** | **124.308** | **Best Fit (Relatif Terbaik)** |
| Gamma | 125.589 | Cocok |
| Weibull | 125.834 | Cukup Cocok |
| Exponential | 129.588 | Kurang Cocok |
| Normal | 150.289 | Paling Tidak Cocok |

> **Kesimpulan Utama:** Distribusi **Log-Normal** terbukti secara matematis merupakan model relatif terbaik dibanding kandidat lainnya karena memiliki nilai AIC paling rendah dengan keunggulan yang signifikan ($\Delta\text{AIC} > 10$).

---

## 🖼️ Pemodelan Log-Normal

### 1. Probability Density Function (PDF)
PDF menunjukkan tingkat kepadatan probabilitas pada nilai *win_odds* tertentu. Kurva Log-Normal teoretis (garis merah) secara presisi menangkap lonjakan probabilitas di area odds kecil (kuda unggulan) sekaligus melandai mengikuti ekor data (*long-tail*) untuk kuda *underdog*.
![Probability Density Function (PDF)](jra_pdf_model.png)

### 2. Cumulative Distribution Function (CDF)
CDF menunjukkan probabilitas kumulatif bahwa suatu variabel acak *win_odds* akan bernilai kurang dari atau sama dengan nilai tertentu. Model ini sangat berguna untuk membaca probabilitas *threshold* secara praktis (misalnya: garis mencapai probabilitas ~80% pada odds 120).
![Cumulative Distribution Function (CDF)](jra_cdf_model.png)

---

## 🔍 Evaluasi Metodologi & Batasan Analisis (*Critical Review*)

1. **Provenans Data (Data Provenance):** Data berasal dari agregasi pihak ketiga (Kaggle), bukan API resmi JRA. Validitas bergantung pada kurasi *uploader*.
2. **Karakteristik Uji Kolmogorov-Smirnov (KS-Test):** Meskipun Log-Normal unggul secara relatif (AIC), uji KS memberikan p-value $< 0,05$ (menolak $H_0$ absolut). Hal ini dikarenakan pada ukuran sampel besar ($n > 12.000$), uji KS memiliki *power* yang sangat tinggi sehingga deviasi kecil dari distribusi teoritis akan terdeteksi signifikan. Oleh karena itu, kriteria AIC lebih tepat digunakan untuk perbandingan relatif antar-model.
3. **Penanganan Outlier & Pembatasan Visual:** Sumbu-X pada histogram PDF dan CDF dibatasi hingga batas `300` agar visualisasi kurva utama tetap terfokus. Terdapat sekitar **7,2% data ($> 300$)** yang berada pada ekor panjang (*long-tail*) dan terpotong secara visual, namun seluruh data penuh tetap disertakan dalam perhitungan kriteria AIC dan parameter model.

---

## 🛠️ Cara Menjalankan Kode

1. Pastikan Python 3.x dan *library* yang dibutuhkan sudah terinstal:
   ```bash
   pip install pandas numpy matplotlib scipy