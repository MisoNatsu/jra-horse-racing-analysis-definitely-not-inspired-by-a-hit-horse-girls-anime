import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings

warnings.filterwarnings('ignore')

# Memuat data
df = pd.read_csv('jra_race_results_2024.csv')
data = df['win_odds'].dropna()

# Kalkulasi parameter Log-Normal
shape, loc, scale = stats.lognorm.fit(data, floc=0)
mu = np.log(scale)
sigma = shape
x = np.linspace(0.1, 300, 1000)

# Membuat Plot PDF
plt.figure(figsize=(8, 6))
plt.hist(data, bins=500, density=True, alpha=0.5, color='steelblue', label='Empirical PDF (Data Aktual)')
pdf_theoretical = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
plt.plot(x, pdf_theoretical, 'r-', lw=2.5, label='Theoretical PDF (Log-Normal)')

plt.xlim(0, 300)
plt.title('Probability Density Function (PDF)\nDistribusi Win Odds', fontsize=14, pad=15)
plt.xlabel('Win Odds', fontsize=12)
plt.ylabel('Densitas Probabilitas', fontsize=12)
plt.legend(fontsize=11)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Menyimpan gambar
plt.savefig('jra_pdf_model.png')
print(f"File jra_pdf_model.png berhasil disimpan! (mu={mu:.4f}, sigma={sigma:.4f})")