import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings

# Mengabaikan warning agar output lebih bersih
warnings.filterwarnings('ignore')

# 1. Membaca dataset dan mengisolasi data
df = pd.read_csv('jra_race_results_2024.csv')
data = df['win_odds'].dropna()

# 2. Setup ukuran kanvas visualisasi
plt.figure(figsize=(10, 6))

# 3. Membuat Histogram (Densitas probabilitas, bukan frekuensi absolut)
plt.hist(data, bins=100, density=True, alpha=0.6, color='steelblue', label='Data aktual (histogram)')

# 4. Fitting Distribusi Log-Normal (Distribusi Terbaik)
shape, loc, scale = stats.lognorm.fit(data)
x = np.linspace(0, data.max(), 1000)
pdf_lognorm = stats.lognorm.pdf(x, shape, loc=loc, scale=scale)
plt.plot(x, pdf_lognorm, 'r-', linewidth=2.5, label='Fit lognorm (AIC=124308)')

# 5. Fitting Distribusi Normal (Sebagai Pembanding)
mu, std = stats.norm.fit(data)
pdf_norm = stats.norm.pdf(x, mu, std)
plt.plot(x, pdf_norm, 'g--', linewidth=2.5, label='Fit normal (AIC=150289)')

# 6. Kustomisasi Tampilan Grafik
plt.xlim(0, 300) # Membatasi sumbu X agar outlier ekstrem tidak merusak visual
plt.title('Distribusi Odds Kemenangan (Win Odds) Kuda Pacu\nJRA Horse Racing 2024', fontsize=14, pad=15)
plt.xlabel('Win Odds', fontsize=12)
plt.ylabel('Densitas Probabilitas', fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# 7. Menampilkan hasil
plt.show()